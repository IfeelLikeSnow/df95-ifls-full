# DF95 FX-Chain Naming Guide (v43)

Dieses Dokument schlägt konkrete Namen für FX-Chains vor, die mit der
v42/v43-Namenslogik und den ImGui-Chain-Browsern kompatibel sind.

Die Präfixe:

- `MIC_...`         → MicFX- und Mikrofon-Korrektur-Chains
- `FX_GLITCH_...`   → Glitch / IDM / Stutter / Slice / Granular
- `FX_PERC_...`     → Percussion / DrumGhost / transientbetonte Chains
- `FX_FILTER_...`   → Filter / Motion / Sweeps / Movement
- `COLOR_...`       → Coloring / Tape / Saturation / Tone-Shaping
- `MASTER_...`      → Mastering / Safety / Limiter / LUFS

## Beispiele pro Kategorie

### MicFX

- `MIC_MD400_Neutral`
- `MIC_NTG4P_ShotgunOutdoor`
- `MIC_MCM_Telecoil_Studio`
- `MIC_GEOFON_DeepLow`
- `MIC_LAV_VO_Clean`
- `MIC_XY_StereoWide`

### Glitch / IDM

- `FX_GLITCH_01_GrainSmear`
- `FX_GLITCH_02_SlicerSync`
- `FX_GLITCH_03_BufferStutter`
- `FX_GLITCH_04_DigitalCrack`
- `FX_GLITCH_05_ReverseFragments`

### Perc / DrumGhost

- `FX_PERC_01_TransientPunch`
- `FX_PERC_02_DrumGhostRoom`
- `FX_PERC_03_LowBoomDesign`
- `FX_PERC_04_ClackSharp`

### Filter / Motion

- `FX_FILTER_01_SlowSweep`
- `FX_FILTER_02_RhythmChop`
- `FX_FILTER_03_BandpassMotion`
- `FX_FILTER_04_DopplerShift`

### Coloring / Tone

- `COLOR_01_TapeWarm`
- `COLOR_02_ConsoleGlue`
- `COLOR_03_DarkFilmTone`
- `COLOR_04_AirBright`
- `COLOR_05_VintageSoftClip`

### Master / Safety

- `MASTER_01_SafetyLimiter`
- `MASTER_02_LUFS_Preview`
- `MASTER_03_CleanGlue`
- `MASTER_04_AltColorMaster`

Diese Namen sind so gewählt, dass sie:

- klar einer Kategorie zugeordnet werden können
- in den ImGui-Dropdowns sortiert und gruppiert erscheinen
- in großen Sessions schnell wiedererkannt werden.

Du kannst frei weitere Chains nach diesem Schema ergänzen.


## 10. Aktuelle Chains im Paket und Zuordnung

- `COLOR_Coloring_Standard.RfxChain` → **Coloring / Tone**
- `Coloring_Standard.RfxChain` → **Coloring / Tone**
- `MASTER_Safety_Highpass.RfxChain` → **Master / Safety**
- `Safety_Highpass.RfxChain` → **Master / Safety**


## 11. Hinweis zur Integration in die DF95-Buttons (v45)

Die ImGui-Chain-Browser-Skripte (MicFX / FXBus / Coloring / Master) durchsuchen
rekursiv den kompletten `FXChains`-Ordner im REAPER-ResourcePath – inklusive
aller Unterordner wie `FXChains/DF95/...`.

Damit stehen *alle* im Repo vorhandenen FX-Chains über die Toolbar-Buttons
zur Verfügung, solange sie im FXChains-Ordner liegen.

Die Kategorisierung erfolgt weiterhin über die Dateinamen:
- MIC_..., FX_GLITCH_..., FX_PERC_..., FX_FILTER_..., COLOR_..., MASTER_...
und thematisch ähnliche Namen.


## 12. MobileFR / S24U Chains (v48)

Für das Script `DF95_Explode_AutoBus_MobileFR.lua` wurden zwei Basis-Chains
hinzugefügt:

- `DF95_FXBus_FieldRecorder_S24U_Atmos_01.RfxChain`
- `DF95_FXBus_FieldRecorder_S24U_Clean_01.RfxChain`

Diese dienen als Startpunkt für Atmos-/Clean-Bearbeitung mobiler Aufnahmen und
können bei Bedarf durch deine eigenen Ketten ersetzt oder erweitert werden.
