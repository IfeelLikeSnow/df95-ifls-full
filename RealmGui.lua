-- DF95/IFLS shim: compatibility layer for scripts that call require("RealmGui")
-- Place this file in: %APPDATA%\REAPER\Scripts\RealmGui.lua
--
-- This maps "RealmGui" to ReaImGui (reaper.ImGui_* API).
-- Requires: ReaImGui extension installed (cfillion) and REAPER restarted.

if not (reaper and reaper.ImGui_CreateContext) then
  reaper.MB(
    "ReaImGui Extension fehlt.\n\nBitte per ReaPack installieren: 'ReaImGui: ReaScript binding for Dear ImGui' (cfillion)\nund REAPER neu starten.",
    "DF95/IFLS",
    0
  )
  return nil
end

return reaper
