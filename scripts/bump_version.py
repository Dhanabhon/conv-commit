#!/usr/bin/env python3
import argparse
import json
import re
from datetime import date
from pathlib import Path


VERSION_FILES = [
    Path("plugin.json"),
    Path("package.json"),
    Path(".codex-plugin/plugin.json"),
    Path(".claude-plugin/plugin.json"),
]


def bump_version(version, part):
    if part == "build":
        part = "patch"
    major, minor, patch = map(int, version.split("."))
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def read_current_version():
    data = json.loads(VERSION_FILES[0].read_text())
    return data["version"]


def write_version(path, version):
    data = json.loads(path.read_text())
    data["version"] = version
    path.write_text(json.dumps(data, indent=2) + "\n")


def update_changelog(version, release_date):
    path = Path("CHANGELOG.md")
    text = path.read_text()
    marker = "## [Unreleased]"
    start = text.index(marker) + len(marker)
    match = re.search(r"\n## \[", text[start:])
    end = start + match.start() if match else len(text)
    unreleased = text[start:end].strip()
    if not unreleased:
        raise SystemExit("CHANGELOG.md has no [Unreleased] notes to release")
    released = f"\n\n## [{version}] - {release_date}\n\n{unreleased}\n"
    path.write_text(text[:start] + released + text[end:])


def self_test():
    assert bump_version("0.5.0", "patch") == "0.5.1"
    assert bump_version("0.5.0", "build") == "0.5.1"
    assert bump_version("0.5.0", "minor") == "0.6.0"
    assert bump_version("0.5.0", "major") == "1.0.0"


def main():
    parser = argparse.ArgumentParser(description="Bump conv-commit release metadata.")
    parser.add_argument(
        "part",
        nargs="?",
        choices=["build", "patch", "minor", "major"],
        default="patch",
        help="Version segment to bump. 'build' is an alias for SemVer patch.",
    )
    parser.add_argument("--version", help="Set an exact version instead of bumping.")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("self-test ok")
        return

    version = args.version or bump_version(read_current_version(), args.part)
    for path in VERSION_FILES:
        write_version(path, version)
    update_changelog(version, args.date)
    print(version)


if __name__ == "__main__":
    main()
