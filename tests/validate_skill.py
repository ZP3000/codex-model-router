"""Validate the installable codex-model-router Skill without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skill" / "codex-model-router"
SKILL_FILE = SKILL_DIR / "SKILL.md"
OPENAI_FILE = SKILL_DIR / "agents" / "openai.yaml"


REQUIRED_FILES = (
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    ".gitignore",
    ".gitattributes",
    ".editorconfig",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/pull_request_template.md",
    ".github/workflows/validate.yml",
    "tests/validate_skill.py",
    "skill/codex-model-router/SKILL.md",
    "skill/codex-model-router/agents/openai.yaml",
    "skill/codex-model-router/references/source-policy.zh-CN.md",
)


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")
        raise AssertionError  # pragma: no cover


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        fail("SKILL.md frontmatter must have a closing delimiter")
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.fullmatch(r"([A-Za-z0-9_-]+):\s*(.+)", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"\'')
    return values


def check_required_files() -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"required file is missing: {relative}")


def check_skill_frontmatter() -> None:
    text = read(SKILL_FILE)
    values = parse_frontmatter(text)
    if values.get("name") != "codex-model-router":
        fail("frontmatter name must be codex-model-router")
    description = values.get("description", "")
    if not description:
        fail("frontmatter description must be non-empty")
    for phrase in ("multi-step", "explicit", "delegation"):
        if phrase not in description.lower():
            fail(f"description must cover {phrase!r} invocation boundary")


def check_local_markdown_links() -> None:
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = read(path)
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.is_file():
                fail(
                    f"broken local Markdown link in {path.relative_to(ROOT)}: {target}"
                )


def check_openai_metadata() -> None:
    text = read(OPENAI_FILE)
    if not re.search(r"(?m)^\s*policy:\s*$", text):
        fail("openai.yaml must define policy")
    if not re.search(r"(?m)^\s*allow_implicit_invocation:\s*true\s*$", text):
        fail("openai.yaml must allow implicit invocation")
    match = re.search(r'(?m)^\s*default_prompt:\s*"([^"]+)"\s*$', text)
    if not match or "$codex-model-router" not in match.group(1):
        fail("default_prompt must explicitly mention $codex-model-router")
    short = re.search(r'(?m)^\s*short_description:\s*"([^"]+)"\s*$', text)
    if not short or not 25 <= len(short.group(1)) <= 64:
        fail("short_description must be present and approximately 25-64 characters")
    if not re.search(r'(?m)^\s*display_name:\s*"[^"]+"\s*$', text):
        fail("display_name must be present")


def check_model_mappings() -> None:
    text = read(SKILL_FILE)
    if "| Profile | model | reasoning_effort |" not in text:
        fail("SKILL.md must expose the routing matrix")
    rows = (
        r"\|\s*Sol Extra High\s*\|\s*`gpt-5\.6-sol`\s*\|\s*`xhigh`\s*\|",
        r"\|\s*Luna Max\s*\|\s*`gpt-5\.6-luna`\s*\|\s*`max`\s*\|",
    )
    for row in rows:
        if not re.search(row, text):
            fail(f"missing exact model mapping: {row}")


def check_source_reference() -> None:
    text = read(SKILL_DIR / "references" / "source-policy.zh-CN.md")
    for phrase in ("核心原则", "标准工作流", "上下文传递", "最高优先级规则"):
        if phrase not in text:
            fail(f"source-policy reference is missing section: {phrase}")


def check_repository_hygiene() -> None:
    """Reject local absolute paths and unfinished placeholders in text files."""
    windows_absolute_path = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:\\")
    term_1 = "TO" + "DO"
    term_2 = "TB" + "D"
    term_3 = "FIX" + "ME"
    unfinished_patterns = (
        (term_1, re.compile(r"\b" + term_1 + r"\b", re.IGNORECASE)),
        (term_2, re.compile(r"\b" + term_2 + r"\b", re.IGNORECASE)),
        (term_3, re.compile(r"\b" + term_3 + r"\b", re.IGNORECASE)),
        (
            "email placeholder",
            re.compile("your-email" + "@" + "example.com", re.IGNORECASE),
        ),
    )
    violations: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            raw = path.read_bytes()
        except OSError as error:
            fail(f"cannot read repository file for hygiene check: {error}")
        if b"\x00" in raw:
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT)
        for match in windows_absolute_path.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            violations.append(f"{relative}:{line} Windows absolute path")
        for label, pattern in unfinished_patterns:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                violations.append(f"{relative}:{line} unfinished placeholder ({label})")
    if violations:
        fail("repository hygiene violations:\n- " + "\n- ".join(violations))


def main() -> int:
    checks = (
        check_required_files,
        check_skill_frontmatter,
        check_local_markdown_links,
        check_openai_metadata,
        check_model_mappings,
        check_source_reference,
        check_repository_hygiene,
    )
    try:
        for check in checks:
            check()
    except AssertionError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(checks)} validation groups; Skill package invariants hold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
