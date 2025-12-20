#!/usr/bin/env python3
import os
import sys
import math
import argparse
import xml.etree.ElementTree as ET
from collections import defaultdict
from copy import deepcopy

def longest_common_dir_prefix(paths):
    """Common prefix trimmed to a directory boundary, e.g. 'Scripts/ReaTeam Scripts/'."""
    if not paths:
        return ""
    pref = os.path.commonprefix(paths)
    # Trim to last slash boundary
    if "/" in pref:
        pref = pref[: pref.rfind("/") + 1]
    else:
        pref = ""
    return pref

def chunk_list(items, size):
    for i in range(0, len(items), size):
        yield items[i:i+size]

def split_reapack_package(reapack_el, max_sources):
    """
    Returns a list of new <reapack> elements (split) if needed,
    otherwise returns [original].
    """
    ver = reapack_el.find("version")
    if ver is None:
        return [reapack_el]

    sources = ver.findall("source")
    if len(sources) <= max_sources:
        return [reapack_el]

    # Extract file paths
    files = [s.get("file", "") for s in sources]
    prefix = longest_common_dir_prefix(files)

    # Group by first folder after prefix
    groups = defaultdict(list)
    for s in sources:
        f = s.get("file", "")
        if prefix and f.startswith(prefix):
            rest = f[len(prefix):]
            group = rest.split("/", 1)[0] if "/" in rest else rest or "(root)"
        else:
            group = "(other)"
        groups[group].append(s)

    # Prepare split packages
    base_name = reapack_el.get("name", "Package")
    ver_attrib = dict(ver.attrib)

    # Keep changelog (if present) at the top of each split version
    changelog = ver.find("changelog")
    changelog_copy = deepcopy(changelog) if changelog is not None else None

    new_packages = []

    # Sort groups by size (largest first) for determinism
    for group_name, group_sources in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
        # Further chunk within group if still too big
        parts = list(chunk_list(group_sources, max_sources))
        total_parts = len(parts)

        for idx, part_sources in enumerate(parts, start=1):
            new_reapack = ET.Element("reapack", attrib=dict(reapack_el.attrib))
            # Rename package
            name = f"{base_name} – {group_name}"
            if total_parts > 1:
                name += f" ({idx}/{total_parts})"
            new_reapack.set("name", name)

            new_ver = ET.SubElement(new_reapack, "version", attrib=ver_attrib)

            if changelog_copy is not None:
                new_ver.append(deepcopy(changelog_copy))

            # Append sources for this split
            for s in part_sources:
                new_ver.append(deepcopy(s))

            new_packages.append(new_reapack)

    return new_packages

def indent(elem, level=0):
    # Pretty-print indentation for readability.
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="infile", default="index.xml")
    ap.add_argument("--out", dest="outfile", default="index.xml")
    ap.add_argument("--max-sources", type=int, default=500)
    ap.add_argument("--only-prefix", default="", help="Optional: only split packages whose name starts with this prefix.")
    args = ap.parse_args()

    tree = ET.parse(args.infile)
    root = tree.getroot()

    # Walk categories and replace large packages
    for cat in root.findall(".//category"):
        repl = []
        for child in list(cat):
            if child.tag != "reapack":
                repl.append(child)
                continue

            name = child.get("name", "")
            if args.only_prefix and not name.startswith(args.only_prefix):
                repl.append(child)
                continue

            ver = child.find("version")
            sources = ver.findall("source") if ver is not None else []
            if len(sources) > args.max_sources:
                split_pkgs = split_reapack_package(child, args.max_sources)
                repl.extend(split_pkgs)
            else:
                repl.append(child)

        # Clear and re-append
        cat[:] = repl

    indent(root)
    tree.write(args.outfile, encoding="utf-8", xml_declaration=True)
    print(f"Wrote {args.outfile} with max_sources={args.max_sources}")

if __name__ == "__main__":
    main()
