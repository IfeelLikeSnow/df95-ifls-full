
# DF95 V77 – ReampSuite Dashboard GUI

Dieses Add-on ergänzt dein bestehendes DF95-/ReampSuite-Setup um ein zentrales,
ImGui-basiertes Dashboard für alle Reamp-bezogenen Workflows (V71–V76.2).

Es baut ausschließlich auf vorhandenen Scripts auf und führt keine eigene
Routing- oder DSP-Logik ein – es ist ein "Hub" über deinen existierenden Modulen.

---

## Inhalt

- `Scripts/IFLS/DF95/ReampSuite/DF95_ReampSuite_Dashboard_GUI.lua`  
  ImGui-GUI, die folgende Informationen/Actions bündelt:

  - Aktives Reamp-Profil (Key, Name, Interface, Out/In-Kanäle)
  - Aktive PedalChain (Key, Name, Use-Case) aus `DF95_REAMP/*` ExtStates
  - Latenz-Offset (Samples + ms) aus `DF95_REAMP/OFFSET_SAMPLES_<PROFILE>`
  - Liste der Reamp-Kandidaten im Projekt (Tracks mit REAMP/DI/PEDAL im Namen)
  - Buttons für:
    - `DF95_V76_SuperPipeline.lua`
    - `DF95_ReampSuite_Router.lua`
    - `DF95_ReampSuite_PedalChains_GUI.lua`
    - `DF95_ReampSuite_LatencyHelper.lua`
    - `DF95_ReampSuite_ApplyLatencyOffset.lua` (V76.2)

- `Documentation/DF95_V77_ReampSuite_Dashboard_GUI.md`  
  Diese Datei.

---

## Voraussetzungen

- DF95-Repo inkl.:
  - `DF95_ReampSuite_Profiles.lua`
  - `DF95_ReampSuite_Router.lua`
  - `DF95_ReampSuite_PedalChains.lua`
  - `DF95_ReampSuite_PedalChains_GUI.lua`
  - `DF95_ReampSuite_LatencyHelper.lua`
  - `DF95_ReampSuite_ApplyLatencyOffset.lua` (V76.2)
  - `DF95_V76_SuperPipeline.lua` (V76 / V76.1)

- ReaImGui muss installiert sein (sonst bricht das Script mit einer Meldung ab).

---

## Installation

1. Dieses Add-on in deinen REAPER-ResourcePath kopieren:

   - `Scripts/IFLS/DF95/ReampSuite/DF95_ReampSuite_Dashboard_GUI.lua`
   - `Documentation/DF95_V77_ReampSuite_Dashboard_GUI.md` (optional)

2. In REAPER:

   - `Actions → Show action list…`
   - `New Action… → Load ReaScript…`
   - `DF95_ReampSuite_Dashboard_GUI.lua` auswählen
   - Action registrieren

3. Optional: in eine Toolbar einbinden, z. B. in deine ReampSuite- oder V76-Toolbar:

   - Label: `ReampSuite Dashboard`
   - Action: `DF95_ReampSuite_Dashboard_GUI`

---

## Bedienkonzept

### 1. Reamp-Profil

- Zeigt das aktive Profil basierend auf `DF95_ReampSuite_Profiles.lua`:
  - Profil-Key (z. B. `UR22_DI_Pedals`)
  - Name (`UR22mkII → DI/Pedals`)
  - Interface (`Steinberg UR22mkII`)
  - Out-/In-Kanäle

- Button **"Profil wählen / Router öffnen"**:
  - ruft `DF95_ReampSuite_Router.lua` per `dofile(...)` auf
  - dort kannst du wie gewohnt Profile wählen und Routing setzen.

### 2. PedalChain Preset

- Liest die aktuellen PedalChain-ExtStates:

  - `DF95_REAMP/PEDAL_CHAIN_KEY`
  - `DF95_REAMP/PEDAL_CHAIN_NAME`
  - `DF95_REAMP/PEDAL_CHAIN_DESC`

- Zeigt Key, Name und Use-Case, sofern gesetzt.

- Button **"PedalChains GUI öffnen"**:
  - ruft `DF95_ReampSuite_PedalChains_GUI.lua` auf
  - dort kannst du Presets auswählen/wechseln.

### 3. Latency / Offset

- Nutzt das aktive Profil, um zu prüfen, ob ein
  `OFFSET_SAMPLES_<PROFILE_KEY>`-Wert in `DF95_REAMP` existiert.

- Wenn ja:
  - zeigt Samples + umgerechnete Millisekunden bei Projekt-Samplerate.

- Buttons:

  - **"Latency Helper starten"**  
    → `DF95_ReampSuite_LatencyHelper.lua`  
    → zum Messen & Setzen von OFFSET-SAMPLES-Werten.

  - **"Offset auto anwenden"**  
    → `DF95_ReampSuite_ApplyLatencyOffset.lua` (V76.2)  
    → verschiebt ReampReturn-Items entsprechend des Offsets.

### 4. Reamp-Kandidaten

- Scannt das Projekt und zeigt eine Liste von Tracks, deren Name eines der
  folgenden Muster enthält:

  - `REAMP`, `RE-AMP`, ` DI `, `_DI`, `DI_`, `PEDAL`

- Dies ist nur eine Anzeige – die eigentliche Logik bleibt in:
  - `DF95_V76_SuperPipeline.lua`
  - `DF95_ReampSuite_MainGUI.lua` (falls vorhanden).

- Button **"V76 SuperPipeline (Fieldrec + Reamp) starten"**:
  - ruft `DF95_V76_SuperPipeline.lua` auf und nutzt deinen bestehenden
    Intelligence/SuperPipeline-Flow.

---

## Hinweise

- Dieses Dashboard fügt keine neue Business-Logik hinzu – es ist eine
  komfortable Oberfläche für die bereits bestehenden Bausteine.

- Falls eines der referenzierten Scripts fehlt oder fehlschlägt,
  wird eine verständliche Fehlermeldung mit Pfad angezeigt.

- Alles läuft in REAPER als klassisches ImGui-Fenster mit `defer`-Loop,
  d. h. du kannst das Fenster geöffnet lassen, während du arbeitest.

---

Viel Spaß mit deinem DF95 ReampSuite Dashboard (V77) –
dein zentrales Cockpit für Profil, Chains, Latenz und SuperPipeline 🚀
