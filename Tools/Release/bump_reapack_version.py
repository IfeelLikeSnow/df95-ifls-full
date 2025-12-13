#!/usr/bin/env python3
"""
DF95 ReaPack version bump helper.

Updates:
- index.xml: all <version name="..."> nodes -> new version
- index.xml: all <version ... time="..."> -> current UTC epoch seconds

Usage:
  python3 Tools/Release/bump_reapack_version.py 3.0.1
"""
from __future__ import annotations

import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
INDEX_XML = REPO_ROOT / "index.xml"

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: bump_reapack_version.py X.Y.Z[-prerelease]")
        return 2

    new_ver = sys.argv[1].strip()
    if not new_ver:
        print("Error: empty version")
        return 2

    if not INDEX_XML.exists():
        print(f"Error: index.xml not found at {INDEX_XML}")
        return 2

    tree = ET.parse(INDEX_XML)
    root = tree.getroot()

    epoch = int(time.time())

    changed = 0
    for ver in root.iter("version"):
        # ReaPack uses <version name="..." time="..."> under packages
        if ver.get("name") != new_ver:
            ver.set("name", new_ver)
            changed += 1
        ver.set("time", str(epoch))

    if changed == 0:
        # still updated time, but name already matched everywhere
        print(f"Version already '{new_ver}' in all <version> nodes; updated time.")
    else:
        print(f"Updated {changed} <version> nodes to '{new_ver}' and refreshed time.")

    # Keep formatting readable (ElementTree is minimal); write as UTF-8.
    tree.write(INDEX_XML, encoding="utf-8", xml_declaration=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
