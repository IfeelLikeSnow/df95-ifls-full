# DF95 SemVer-Regeln (empfohlen)

Quelle: Semantic Versioning 2.0.0 (MAJOR.MINOR.PATCH).  
- **MAJOR** erhöhen, wenn sich die *öffentliche Bedien-/API-Oberfläche* inkompatibel ändert (Breaking Change).
- **MINOR** erhöhen, wenn neue Funktionen *abwärtskompatibel* hinzukommen.
- **PATCH** erhöhen, wenn *abwärtskompatible Bugfixes* erfolgen.  

## Was ist bei DF95 „öffentlich“ (entscheidet MAJOR vs. MINOR/PATCH)

Als „public surface“ gilt alles, worauf User/Setups typischerweise verlinken:

- **Action-Skripte / Entry-Points** (Dateinamen, Action-IDs, erwartete Parameter)
- **Hub-Namen & Menüpfade** (was im Master-Menü sichtbar ist)
- **Config-Keys/Feature-Flags** (z.B. Support/DF95_Config.json)
- **CSV/JSON Katalog-Schemata** (Spalten/Keys, die User editieren)

**Breaking (MAJOR):**
- Entry-Script umbenennen/entfernen
- Hub-ID umbenennen/entfernen
- Config-Key entfernen oder Bedeutung ändern
- CSV/JSON Feld umbenennen/anders interpretieren
- Legacy-Fallback entfernen, wenn User es noch brauchen

**MINOR (Feature Add):**
- neue Hubs, neue Menüpunkte
- neue optionale Config-Keys (mit Defaults)
- neue Tools im Folder-Scan

**PATCH (Bugfix):**
- Fixes in Hub-UX, RequireRules, Adapter, SmokeTest
- Robustheit/Performance ohne sichtbare Workflow-Änderung

## Pre-releases (optional)
Für Testreleases: `3.1.0-rc.1`, `3.1.0-rc.2` etc.  
Wenn ihr pre-releases nutzt: erst final `3.1.0` releasen, wenn RC stabil.

