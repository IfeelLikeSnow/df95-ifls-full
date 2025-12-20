#!/usr/bin/env python3
import os, time, math
import xml.etree.ElementTree as ET
from collections import defaultdict

BRANCH = "main"
RAW_BASE = "https://raw.githubusercontent.com/IfeelLikeSnow/df95-ifls-full/" + BRANCH + "/"

MAX_SOURCES = 500  # Strategie-B Stabilitätslimit

def indent(elem, level=0):
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

def list_files(root, prefixes):
    files=[]
    for pfx in prefixes:
        abs_pfx = os.path.join(root, pfx)
        if not os.path.isdir(abs_pfx):
            continue
        for dp,_,fns in os.walk(abs_pfx):
            for fn in fns:
                # ggf. Filter: nur relevante ReaPack-Dateitypen
                if fn.startswith("."):
                    continue
                rel = os.path.relpath(os.path.join(dp, fn), root).replace("\\","/")
                files.append(rel)
    return sorted(set(files))

def add_package(cat_el, name, desc, files, author, version):
    rp = ET.SubElement(cat_el, "reapack", attrib={
        "name": name,
        "type": "script",
        "desc": desc
    })
    md = ET.SubElement(rp, "metadata")
    ET.SubElement(md, "description").text = desc

    ver_el = ET.SubElement(rp, "version", attrib={
        "name": version,
        "author": author,
        "time": str(int(time.time()))
    })
    for f in files:
        src = ET.SubElement(ver_el, "source", attrib={"file": f})
        src.text = RAW_BASE + f
    return rp

def chunked(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

def split_by_subfolder(files, prefix):
    """
    Groups by first folder under prefix.
    Example: prefix 'Scripts/ReaTeam Scripts/' groups by 'MIDI Editor', 'Items', ...
    """
    groups = defaultdict(list)
    for f in files:
        if not f.startswith(prefix):
            groups["(other)"].append(f)
            continue
        rest = f[len(prefix):]
        key = rest.split("/",1)[0] if "/" in rest else "(root)"
        groups[key].append(f)
    return groups

def build():
    repo_root = os.getcwd()

    index = ET.Element("index", attrib={
        "version": "1",
        "name": "DF95 IFLS V3",
        "desc": "DF95 IFLS V3 Full (Core + Third-party bundles, auto-split)"
    })

    # === 1) Eigene Kategorien wie im Core-Repo (Beispiel, passe Prefixes an deine Struktur an) ===
    # Du musst hier nur die Ordnerliste korrekt auf dein Full-Repo mappen.
    own_layout = [
        ("DF95/01 Core",   "DF95 V3 - Core (Full)",      "Core framework + essentials", ["Scripts/DF95Framework", "Scripts/DF95 IFLS V3"]),
        ("DF95/05 Resources","DF95 V3 - Resources Pack","MenuSets/Resources",          ["MenuSets", "Resources"]),
        ("IFLS",           "IFLS - Bundle",              "IFLS scripts bundle",         ["Scripts/IFLS"]),
    ]

    for cat_name, pkg_name, pkg_desc, prefixes in own_layout:
        cat = ET.SubElement(index, "category", attrib={"name": cat_name})
        files = list_files(repo_root, prefixes)
        if files:
            add_package(cat, pkg_name, pkg_desc, files, author="IfeelLikeSnow", version="3.0.0")

    # === 2) Third-party: ReaTeam/MPL/X-Raym/Cockos splitten ===
    thirdparty = [
        ("Third-party/ReaTeam", "Scripts/ReaTeam Scripts/", "ReaTeam Scripts"),
        ("Third-party/MPL",     "Scripts/MPL Scripts/",     "MPL Scripts"),
        ("Third-party/X-Raym",  "Scripts/X-Raym Scripts/",  "X-Raym Scripts"),
        ("Third-party/Cockos",  "Scripts/Cockos/",          "Cockos Scripts"),
    ]

    for cat_name, prefix, label in thirdparty:
        files = list_files(repo_root, [prefix.rstrip("/")])
        if not files:
            continue

        cat = ET.SubElement(index, "category", attrib={"name": cat_name})
        groups = split_by_subfolder(files, prefix)

        for group, gfiles in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
            # chunk if still too large
            parts = list(chunked(sorted(gfiles), MAX_SOURCES))
            total = len(parts)
            for i, part in enumerate(parts, start=1):
                suffix = f" – {group}"
                if total > 1:
                    suffix += f" ({i}/{total})"
                add_package(
                    cat,
                    name=f"{label}{suffix}",
                    desc=f"{label} ({group}) auto-split",
                    files=part,
                    author="IfeelLikeSnow",
                    version="3.0.0"
                )

    indent(index)
    ET.ElementTree(index).write("index.xml", encoding="utf-8", xml_declaration=True)
    print("Wrote index.xml")

if __name__ == "__main__":
    build()
