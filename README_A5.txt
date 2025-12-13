DF95 IFLS V3 – A5 Patch
======================

Purpose
- Refine RequireRules for action-based dependencies (NamedCommandLookup string IDs).
- Adds second-pass inference: _SWS*, _S&M*, _JS_*, _REAPACK*.
- Keeps uniform causes labels (requires ...), relying on existing hub policy.

Files included
- Scripts/DF95Framework/Lib/DF95_RequireRules.lua  (updated)
- Scripts/DF95Framework/Menus/DF95_Hubs.lua        (patched integration points / example usage)

Notes
- This patch assumes your existing V3 repo already has:
  - DF95_Capabilities.lua
  - DF95_MenuBuilder.lua with disabled label support
  - Hub renderer that respects item.disabled + item.disabled_reason
- Merge by overwriting the files in the same relative paths.
