# DF95 V72 – SuperPipeline + Reamp Fusion (Intelligence Layer)

Dieses Paket erweitert V71/V70 um:

- `DF95_V72_SuperPipeline.lua`
  - Orchestriert:
    - Fieldrec/Dialog/FX-Tracks → DF95 Auto SuperPipeline (MicFX + ExportTags)
    - Reamp-Kandidaten (Trackname enthält z.B. "REAMP", "DI", "PEDAL") → DF95_V71_ReampRouter.lua

- `DF95_V71_ReampRouter.lua`
  - Legt für ausgewählte Reamp-Tracks eine einfache Reamp-Konfiguration an:
    - Source Track → Hardware Out (DF95_REAMP/OUT_CH, Default 3)
    - Neuer Return Track → Hardware In (DF95_REAMP/IN_CH, Default 1)
  - Achtet darauf, dass OUT_CH != IN_CH (Warnung bei Konflikt).

- `DF95_V71_LatencyAnalyzer.lua`
  - Erstellt einen Testimpuls-Track und erklärt, wie man manuell die Reamp-Latenz misst
    und in DF95_REAMP/OFFSET_SAMPLES hinterlegt.

## Verwendung

1. Installiere zunächst ein vollständiges DF95-Repo mit:
   - AutoMic/Auto SuperPipeline (V69/V70)
   - Reamp-Tools (frühere Versionen, falls vorhanden)

2. Kopiere die Inhalte dieses V72-Repos in deinen REAPER-ResourcePath (über vorhandene DF95-Scripts drüber oder in einen dedizierten Entwicklungsordner).

3. Lade die Scripts in REAPER:
   - `DF95_V72_SuperPipeline.lua`
   - `DF95_V71_ReampRouter.lua`
   - `DF95_V71_LatencyAnalyzer.lua`

4. Importiere die Toolbar:
   - `Toolbars/DF95_V72_SuperPipeline_Reamp_Toolbar.ReaperMenuSet`
   - z.B. als Toolbar 10 und binde sie bei Bedarf an den DF95 Toolbar Switcher.

5. Workflow-Idee:
   - Tracks benennen (z.B. `ZF6_MD400_Dialog`, `GTR_DI_Reamp`, `FXStem_Pedal_Reamp`).
   - Alle relevanten Tracks selektieren.
   - `V72 SuperPipeline` ausführen:
     - Fieldrec/Dialog → MicFX+ExportTags via DF95_Auto_SuperPipeline.lua
     - Reamp Tracks → DF95_V71_ReampRouter konfiguriert HW Routing + Return Tracks.
   - Optional:
     - `V71 Latency Analyzer` nutzen, um den Reamp-Versatz einmalig zu messen.

Hinweis:
- Diese Implementierung ist absichtlich defensiv gehalten:
  - Sie nimmt keine harten Annahmen über dein Interface vor.
  - Sie nutzt ExtStates für Out/In-Kanalwahl und lässt dir die Hoheit über das Feintuning.
- Du kannst jederzeit in DF95_REAMP/OUT_CH, DF95_REAMP/IN_CH und DF95_REAMP/OFFSET_SAMPLES eigene Werte hinterlegen.
