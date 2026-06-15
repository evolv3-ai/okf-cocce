#!/usr/bin/env python3
"""Validate the OKF-COCCE repository."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_REPO_FILES = ["README.md", "AGENTS.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", "spec/index.md", "spec/okf.md", "spec/cocce.md", "spec/conformance.md", "spec/versioning.md"]
REQUIRED_OKF_FILES = ["okf/index.md", "okf/log.md", "okf/cocce.md"]
REQUIRED_OKF_DIRS = ["categories", "objects", "capabilities", "integrations", "connections", "events", "policies", "playbooks", "references"]
CONCEPT_TYPES = {"Category", "ObjectType", "Object", "Capability", "Integration", "Connection", "Event", "Policy", "Playbook", "Reference"}
SECRET_PATTERNS = [re.compile(p, re.I) for p in [r"secret\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{12,}", r"token\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{12,}", r"password\s*[:=]", r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----", r"ghp_[A-Za-z0-9]{20,}", r"sk-[A-Za-z0-9]{20,}"]]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

class ValidationError(Exception):
    pass

def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValidationError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValidationError(f"{path}: unterminated YAML frontmatter")
    raw = text[4:end]
    data = {}
    current = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current:
            data.setdefault(current, []).append(line[4:].strip().strip('"\''))
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current = key
            if value == "":
                data[key] = []
            elif value.startswith("[") and value.endswith("]"):
                data[key] = [v.strip().strip('"\'') for v in value[1:-1].split(",") if v.strip()]
            else:
                data[key] = value.strip('"\'')
    if not str(data.get("type", "")).strip():
        raise ValidationError(f"{path}: missing required type field")
    return data, text[end + 4:]

def is_reserved(path: Path) -> bool:
    return path.name in {"index.md", "log.md"}

def validate_links(root: Path, path: Path, text: str):
    for target in LINK_RE.findall(text):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (root / target.lstrip("/")) if target.startswith("/") else (path.parent / target)
        if target.endswith("/"):
            resolved = resolved / "index.md"
        if not resolved.exists():
            raise ValidationError(f"{path}: broken internal link to {target}")

def validate_secret_free(path: Path, text: str):
    if "connections" not in path.parts:
        return
    lowered = text.lower()
    allowed_markers = ["secret_ref", "secret reference", "environment variable", "vault path", "never secret values"]
    for pattern in SECRET_PATTERNS:
        if pattern.search(text) and not any(m in lowered for m in allowed_markers):
            raise ValidationError(f"{path}: possible secret value in connection document")

def validate(root: Path) -> list[str]:
    errors = []
    for rel in REQUIRED_REPO_FILES + REQUIRED_OKF_FILES:
        if not (root / rel).exists():
            errors.append(f"missing required file: {rel}")
    for rel in REQUIRED_OKF_DIRS:
        if not (root / "okf" / rel).is_dir():
            errors.append(f"missing required okf directory: okf/{rel}")
    for path in root.rglob("*.md"):
        if any(part in {".git", "node_modules", ".venv"} for part in path.parts):
            continue
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        try:
            if not is_reserved(path) and (rel.parts[0] in {"okf", "examples"}):
                fm, body = parse_frontmatter(path)
                typ = fm.get("type")
                if typ in CONCEPT_TYPES:
                    if typ == "Category" and not fm.get("category"):
                        raise ValidationError(f"{rel}: Category requires category")
                    if typ == "ObjectType" and not all(fm.get(k) for k in ["category", "object", "object_type"]):
                        raise ValidationError(f"{rel}: ObjectType requires category, object, object_type")
                    if typ == "Capability" and not all(fm.get(k) for k in ["category", "object", "object_type", "action", "capability"]):
                        raise ValidationError(f"{rel}: Capability requires category, object, object_type, action, capability")
                validate_secret_free(rel, text)
            validate_links(root, path, text)
        except ValidationError as exc:
            errors.append(str(exc))
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    errors = validate(Path(args.root).resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OKF-COCCE validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
