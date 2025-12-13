# DF95 Auto SuperPipeline (V69)

Die Auto SuperPipeline verbindet die AutoMic-Engine mit:

- Mic-FXChains
- Export/UCS-Tags
- optionalem AutoChainFix
- GUI-Frontend (ImGui)

## Scripts

### 1. DF95_Auto_SuperPipeline.lua

Ein One-Click-Workflow ohne GUI:

- arbeitet auf allen selektierten Tracks
- pro Track:
  - analysiert Name → Recorder/Mic/Pattern/Channels via AutoMicTagger
  - fügt die entsprechende Mic-FXChain ein
- zusätzlich:
  - setzt (projektweit) ExportTags:
    - MicModel
    - RecMedium
    - MicPattern
    - MicChannels

Voraussetzungen:

- `DF95_Auto_MicTagger.lua`
- optional `DF95_Export_Core.lua` (für ExportTags)

Empfohlene Nutzung:

1. Tracks benennen (z. B. `ZF6_MD400_Dialog_Close`, `H5_XYH5_StreetAmb`).
2. Tracks selektieren.
3. Action `DF95: Auto SuperPipeline – MicFX + ExportTags` ausführen.
4. Danach Export-Pipeline (UCS) wie gewohnt verwenden.

### 2. DF95_Auto_SuperPipeline_GUI.lua

ImGui-Variante mit Kontrolle über die Schritte:

- zeigt alle selektierten Tracks mit:
  - Tracknummer, Name
  - erkannter Recorder
  - MicModel
  - Pattern
  - Channels
  - vorgeschlagene FXChain

Optionen:

- [x] Mic-FXChains einfügen
- [x] ExportTags setzen (MicModel/RecMedium/MicPattern/MicChannels)
- [ ] AutoChainFix ausführen (DF95_AutoChain_Fixer.lua)

Button:

- **Run** → führt die gewählten Schritte für alle Tracks aus.

Voraussetzungen:

- ReaImGui
- `DF95_Auto_MicTagger.lua`
- optional `DF95_Export_Core.lua`
- optional `DF95_AutoChain_Fixer.lua`

## Toolbar-Integration (SuperPipeline Button)

Empfohlen:

- In Main- oder Hub-Toolbar eine Action hinzufügen:

  - `DF95_Auto_SuperPipeline.lua` **oder**
  - `DF95_Auto_SuperPipeline_GUI.lua`

Button-Texte:

- `AutoMic ALL` (non-GUI)
- `SuperPipeline` (GUI)

Workflow-Idee:

1. Fieldrec-Dateien auf neue Tracks ziehen.
2. Tracks sinnvoll benennen (Recorder/Mic im Namen).
3. Alle Tracks selektieren.
4. `SuperPipeline`-Button klicken.
5. MicFX, ExportTags und (optional) Chain-Namen sind konsistent.

## Zusammenspiel mit ExportDesk

Nach der SuperPipeline sind:

- MicFX passend eingefügt.
- ExportTags vorbereitet (MicModel, RecMedium etc.).

Im ExportDesk kannst du dann:

- UCS-Namen/Gruppen setzen.
- Export laufen lassen.
- optional `DF95_Export_UCS_MicRecorder_FromTrackname.lua` weiterverwenden, falls du manuell feintunen willst.
