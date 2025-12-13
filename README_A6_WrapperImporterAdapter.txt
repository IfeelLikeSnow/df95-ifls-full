A6 – Wrapper-Importer-Adapter (CSV/JSON/Folder-Scan)

What it does
- Adds a central adapter module: Scripts/DF95Framework/Lib/DF95_WrapperAdapter.lua
- Normalizes action fields into item.actions[] / item.action_strings[]
- Automatically extracts underscore action string IDs from Lua scripts by scanning for:
    reaper.NamedCommandLookup("_SWS_...") etc.
  so A5 RequireRules can infer 'requires' without touching catalogs.

How to integrate (minimal)
1) In Scripts/DF95Framework/Menus/DF95_Hubs.lua (or your hub runner), require the adapter once:
    local Adapter = dofile(base .. "/Scripts/DF95Framework/Lib/DF95_WrapperAdapter.lua")

2) Before applying RequireRules / building menu items, call:
    Adapter.enrich_item(it)

   Do this for:
   - hub.items definitions (kind="script"/"fn"/"hub")
   - any wrapper-imported items (CSV/JSON)
   - folder-scan generated items (if you create items as tables)

Notes
- No catalog changes required.
- The script scan is cached per path to keep menus snappy.
