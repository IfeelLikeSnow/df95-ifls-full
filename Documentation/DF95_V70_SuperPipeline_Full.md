# DF95 V70 – SuperPipeline Full Version

Dieses Paket erweitert V69 um:

- eine eigene DF95 SuperPipeline Toolbar (`Menus/DF95_SuperPipeline_Toolbar.ReaperMenuSet`)
- eine Integration in den Toolbar Switcher (`DF95_Menu_ToolbarSwitcher_ImGui.lua`) als:
  - "DF95 SuperPipeline (Toolbar 9)" in der Kategorie "Core / Hub"

## Nutzung

1. Kopiere den Inhalt dieses Repos in deinen REAPER-ResourcePath.
2. Starte REAPER neu (oder: "Re-scan for new actions").
3. Öffne `Actions → Show action list…` und suche nach:
   - `DF95: Auto SuperPipeline – MicFX + ExportTags`
   - `DF95: Auto SuperPipeline GUI`
4. Toolbar Switcher:
   - In der Main Toolbar gibt es bereits einen Button "Toolbar Switcher (DF95 Toolbars)".
   - Klicke ihn: Im Dropdown siehst du jetzt:
     - "DF95 SuperPipeline (Toolbar 9)" unter "Core / Hub".
   - Wähle den Eintrag, um die neue SuperPipeline-Toolbar als Floating Toolbar (oder oben) anzuzeigen.

5. Toolbar-Inhalt:
   - SuperPipeline GUI
   - SuperPipeline (All Tracks)
   - AutoMic GUI
   - AutoMic (Single Track)
   - Mic Chains Fix (Safe)
   - Export – UCS Mic/Recorder (AutoMicTagger)

Damit hast du einen dedizierten Workspace für:
- AutoMic → MicFX
- AutoMic → ExportTags (MicModel/RecMedium etc.)
- MicChain-Normalisierung

