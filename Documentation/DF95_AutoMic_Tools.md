# DF95 Auto Mic Tools (V68)

Dieses Dokument beschreibt die neuen Auto-Mic-Werkzeuge in V68:

- DF95_Auto_MicTagger.lua
- DF95_AutoMic_Inserter.lua
- DF95_AutoMic_Inserter_GUI.lua
- DF95_AutoChain_Fixer.lua

## AutoMic Inserter GUI

Script: `DF95_AutoMic_Inserter_GUI.lua`

- benötigt ReaImGui
- zeigt alle ausgewählten Tracks mit:
  - Track-Name
  - erkannter Recorder (ZF6, H5, Android, …)
  - Mic-Modell (MD400, NTG4Plus, CM300, XYH5, SGH6, …)
  - Pattern (Cardioid, Supercardioid, XY, Omni, Wide, …)
  - Mono/Stereo
  - vorgeschlagene FXChain (Mic_… .RfxChain)
- Buttons:
  - Refresh (Tracks neu scannen)
  - "Auf alle Tracks Mic-Chain einfügen"
  - "Insert" pro Track

## AutoChain Fixer

Script: `DF95_AutoChain_Fixer.lua`

- nutzt den gleichen MicTagger, um Mic-Chain-Dateinamen zu normalisieren.
- arbeitet im Ordner: `FXChains/DF95/Mic/`
- Standard: DRY RUN (`APPLY = false`)
  - zeigt nur an, welche Umbenennungen möglich wären
  - schreibt eine Liste in die ReaScript Console
- Wenn `APPLY = true` gesetzt wird:
  - benennt die entsprechenden `.RfxChain`-Dateien tatsächlich um
  - siehe `DF95_Chain_Naming_Policy.md` für Richtlinien

Empfohlener Ablauf:

1. V66/V67 Repo in den ResourcePath kopieren.
2. `DF95_AutoChain_Fixer.lua` einmal im DRY RUN ausführen.
3. Wenn alles plausibel aussieht: `APPLY = true` setzen und erneut ausführen.
4. Danach die AutoMic Scripts (GUI oder Non-GUI) nutzen, um neue Projekte zu beschicken.
