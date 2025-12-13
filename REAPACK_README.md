# DF95 IFLS V3 – ReaPack repository (Model B: Core + Packs)

This repository ships **all DF95 V3 functionality** via ReaPack, without removing any scripts/resources.

Packages:
- **DF95 V3 - Core**: framework, hubs, entry actions, diagnostics
- **DF95 V3 - Tools Pack**: auto-discovered tools folder
- **DF95 V3 - Catalogs Pack**: CSV/JSON catalogs (Data/ + Config/)
- **DF95 V3 - Legacy Pack**: legacy fallback scripts/menus
- **DF95 V3 - Resources Pack**: themes, icons, toolbars, FXChains, presets, docs

How users install:
1. In REAPER: Extensions → ReaPack → Import a repository
2. Paste the raw URL to `index.xml` from your hosting (e.g., GitHub raw link)
3. Extensions → ReaPack → Synchronize packages
4. Browse packages → install the packs you want (or all).

Notes:
- The repository `index.xml` is the authoritative manifest for ReaPack.
- Keeping packs separate lets users skip optional assets (e.g., themes) while retaining full DF95 functionality if they install all packs.
