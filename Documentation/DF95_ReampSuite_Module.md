# DF95 ReampSuite (V73) – Modulares Reamp-Modul mit Pedal-Ketten

Dieses Modul ergänzt die V72-SuperPipeline um eine eigenständige ReampSuite:

- Profilverwaltung für Reamp-Routing (UR22/PreSonus/Zoom/Generic)
- GUI-Hub (ReampSuite_MainGUI)
- Latenz-Helper
- Pedal-Ketten-Presets inkl. Tagging

## Scripts

- ReampSuite/DF95_ReampSuite_Profiles.lua
  - definiert Reamp-Profile:
    - UR22_DI_Pedals
    - Presonus_DI_Pedals
    - ZoomF6_Reamp
    - Generic_Reamp
  - verwaltet:
    - DF95_REAMP/PROFILE
    - DF95_REAMP/OUT_CH
    - DF95_REAMP/IN_CH

- ReampSuite/DF95_ReampSuite_Router.lua
  - kleiner Dialog zur Profilwahl
  - setzt OUT_CH/IN_CH gemäß Profil

- ReampSuite/DF95_ReampSuite_LatencyHelper.lua
  - ruft DF95_V71_LatencyAnalyzer.lua auf
  - erklärt, wie OFFSET_SAMPLES_<PROFILE> in DF95_REAMP gespeichert werden kann

- ReampSuite/DF95_ReampSuite_MainGUI.lua
  - ImGui-Fenster:
    - zeigt aktives Profil
    - listet Reamp-Kandidaten (Tracks mit REAMP/DI/PEDAL im Namen)
    - Buttons:
      - Profil wählen
      - V71 ReampRouter
      - Latenz-Helper

## Pedal-Ketten-Presets

- ReampSuite/DF95_ReampSuite_PedalChains.lua
  - enthält vordefinierte Pedal-Ketten:
    - Clean_Ambient
    - Crunch_Drive
    - Bitcrush_Glitch
    - Modulation_Wash
    - Pitch_Space
  - speichert aktives Preset in:
    - DF95_REAMP/PEDAL_CHAIN_KEY
    - DF95_REAMP/PEDAL_CHAIN_NAME
    - DF95_REAMP/PEDAL_CHAIN_DESC
  - Funktion:
    - apply_to_selected_tracks() → hängt z.B. `[PC:Clean_Ambient]` an Track-Namen an

- ReampSuite/DF95_ReampSuite_PedalChains_GUI.lua
  - ImGui-GUI:
    - listet alle Chains mit Name, Use-Case, Pedal-Liste
    - Buttons:
      - „Aktivieren“ → Preset aktiv + ExtStates setzen
      - „Tag auf selektierte Tracks“ → Tagging der aktuell markierten Tracks

## Toolbar

- Toolbars/DF95_ReampSuite_Toolbar.ReaperMenuSet

Enthält Buttons:

- ReampSuite GUI
- ReampSuite – Profil wählen
- ReampSuite – Pedal Chains
- ReampSuite – Latency Helper
- V71 Reamp Router

Diese Toolbar kann als eigene Toolbar importiert und bei Bedarf über deine Main/Hub-Toolbars (z.B. via Toolbar-Switcher) erreichbar gemacht werden.

## IDM-orientierte Pedal-Ketten (V75)

Die Pedal-Ketten wurden für IDM/Glitch/Experimental-Workflows optimiert:

- IDM_GlitchPerc
  - stotternde, bitgecrushte Drums & Percussion
  - Mario Bit Crusher + sehr kurze DD400-Delays (+ ggf. kleiner DR100-Raum)

- IDM_ChipNoise
  - 8-Bit/Retro-Computersound, Noiseflächen, FX-OneShots

- IDM_PitchWarp
  - Whammy-basierte Pitch-Sweeps, pseudo-formantige Leads & FX

- IDM_ModWash
  - modulierte Reverb/Delay-Washes für Pads, Drones, Atmos

- IDM_GranularEcho
  - „granular anmutende“ Echo-Strukturen durch kombiniertes Analog-/Digital-Delay

- Clean_Ambient
  - neutraler, eher cleaner Raum als Rückfallebene, wenn es weniger extrem sein soll

Diese Presets sind als „mentale Templates“ gedacht:
- du erinnerst dich später, welche Hardware-Kette du für einen Sound verwendet hast
- du kannst Re-Recordings und Variationen gezielt auf Basis des gleichen Setups fahren
