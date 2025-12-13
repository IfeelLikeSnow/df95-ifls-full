# DF95 AutoMic Toolbar Integration (V68)

Dieses Dokument beschreibt, wie du die neuen AutoMic-Tools in deine
DF95-Toolbars (Main / Hub / Export Desk) integrieren kannst.

## 1. Relevante Actions / Scripts

Folgende Actions sind für AutoMic relevant:

- `DF95_AutoMic_Inserter_GUI.lua`
  - ImGui-Frontend, das alle selektierten Tracks scannt und passende Mic-Chains vorschlägt / einfügt.

- `DF95_AutoChain_Fixer.lua`
  - Normalisiert Mic-FXChain Dateinamen gemäß DF95_Chain_Naming_Policy
  - Standard: DRY RUN (nur Anzeige).

- `DF95_Export_UCS_MicRecorder_FromTrackname.lua`
  - Nutzt den AutoMicTagger, um UCS-ExportTags
    `MicModel` und `RecMedium` aus Track-Namen vorzubelegen.

## 2. Actions in REAPER registrieren

1. Öffne REAPER.
2. `Actions → Show action list…`
3. Button: **Add… / Load**
4. Navigiere zu:
   `Scripts/IFLS/DF95/`
5. Lade nacheinander:
   - `DF95_AutoMic_Inserter_GUI.lua`
   - `DF95_AutoChain_Fixer.lua`
   - `DF95_Export_UCS_MicRecorder_FromTrackname.lua`

Danach tauchen die Actions in der Action List unter dem jeweiligen Skript-Namen auf.

## 3. Buttons zur Main Toolbar hinzufügen

1. `Options → Customize menus/toolbars…`
2. Im Dropdown oben: **Main toolbar** wählen.
3. Rechts: `Add…` → `Action…`
4. In der Action-Liste:

   - Suche: `DF95_AutoMic_Inserter_GUI`
     - auswählen → `Select`
     - Optional: Icon zuweisen (z. B. ein Mic-Icon aus Data/toolbar_icons/DF95)

   - Suche: `DF95_AutoChain_Fixer`
     - hinzufügen (z. B. im Utility-Bereich der Toolbar)

5. `Save` / `OK`, um die Toolbar zu speichern.

Empfohlene Beschriftungen:

- Button-Text: `AutoMic` für den Inserter
- Button-Text: `Mic Fix` für den Chain Fixer

## 4. Buttons zur DF95 Hub Toolbar hinzufügen

Wenn du eine DF95 Hub Toolbar importiert hast (z. B. `DF95_MainToolbar_FlowErgo_Hub…`):

1. Wieder `Options → Customize menus/toolbars…`
2. Im Dropdown: die entsprechende DF95-Hub-Toolbar auswählen.
3. Analog zu oben:
   - `Add Action…` → `DF95_AutoMic_Inserter_GUI`
   - Optional: `DF95_AutoChain_Fixer`

Positionsempfehlung:

- Bereich „Input / Fieldrec / MicFX“ im Hub
- Beschriftung z. B.:
  - `AutoMic GUI`
  - `Mic Chains Fix`

## 5. Integration in den Export Desk

Falls du einen DF95 Export-Desk (Toolbar) verwendest:

1. `Options → Customize menus/toolbars…`
2. Export-Toolbar im Dropdown auswählen (z. B. `DF95_ExportDesk_MainToolbar`).
3. `Add Action…` → `DF95_Export_UCS_MicRecorder_FromTrackname`
4. Beschriftung:
   - Button-Text: `Mic/Rec (Auto)`
   - Tooltip: „MicModel/RecMedium aus Trackname via AutoMicTagger setzen“

So kannst du vor einem Export:

- die Tracks benennen (z. B. „ZF6_MD400_Dialog_Close“)
- den Button `Mic/Rec (Auto)` drücken
- UCS-ExportTags werden vorbereitet (`MicModel`, `RecMedium`).

## 6. Best Practices

- Track-Namen bei Fieldrecordings so wählen, dass Recorder/Mic erkennbar sind:
  - `ZF6_MD400_Center`
  - `H5_XYH5_Street_Amb`
  - `Android_FieldRec_Kitchen`

- Danach:
  - AutoMic GUI → Mic-Chains einfügen
  - ExportDesk-Button `Mic/Rec (Auto)` → Tags setzen
  - DF95 Export Wizard nutzen wie gewohnt.
