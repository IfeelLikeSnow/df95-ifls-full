
# DF95 V80 – ReampSuite AutoSession (Fully Automated Reamp Session)

Dieses Add-on bringt deinen DF95 ReampSuite-Workflow (V76–V79) auf die nächste Stufe:
eine **weitgehend vollautomatisierte Reamp-Session** für selektierte DI-/Reamp-Quellen.

---

## Inhalt

- `Scripts/IFLS/DF95/ReampSuite/DF95_V80_ReampSuite_AutoSession.lua`  
  Script, das:

  - selektierte DI-/Reamp-Tracks analysiert (Länge der Items)
  - `DF95_V79_ReampSuite_OneClickReamp.lua` aufruft (Routing + PedalChains-Intelligenz)
  - ReampReturn-Tracks einsammelt
  - eine Time Selection über die DI-Region (plus Tail) setzt
  - den Transport auf **Record** schaltet und bis zum Ende der Region laufen lässt
  - nach Ende automatisch stoppt
  - optional:
    - `DF95_ReampSuite_ApplyLatencyOffset.lua` ausführt (V76.2)
    - `DF95_ReampSuite_AutoGain.lua` ausführt (V78)
  - Time Selection & Cursorposition wiederherstellt

- `Documentation/DF95_V80_ReampSuite_AutoSession.md`  
  Diese Datei.

---

## Voraussetzungen

- DF95-ReampSuite-Setup ist installiert, inkl.:
  - `DF95_ReampSuite_Profiles.lua`
  - `DF95_ReampSuite_Router.lua`
  - `DF95_ReampSuite_PedalChains.lua`
  - `DF95_ReampSuite_PedalChains_Intelligence.lua` (AudioIntelligence 2.0 empfohlen)
  - `DF95_V76_SuperPipeline.lua` (optional, aber kompatibel)
  - `DF95_V76_2_ReampSuite_ApplyLatencyOffset.lua`
  - `DF95_ReampSuite_AutoGain.lua`

- V79 OneClickReamp ist installiert:
  - `DF95_V79_ReampSuite_OneClickReamp.lua`

- Die DI-/Reamp-Quellen-Tracks besitzen:
  - sinnvolle Namen (REAMP/DI/PEDAL im Namen)
  - Items, deren Länge die Reamp-Region definieren soll

---

## Funktionsweise im Detail

### 1. Auswahl der Quellen

- Script nutzt **selektierte Tracks** als Ausgangsbasis.
- Daraus werden Reamp-Kandidaten gefiltert:
  - Name enthält (Case-insensitive):
    - `REAMP`
    - `RE-AMP`
    - ` DI `
    - `_DI`
    - `DI_`
    - `PEDAL`

Wenn kein Kandidat gefunden wird, wird abgebrochen.

### 2. Bestimmung der Reamp-Region

- Für alle Reamp-Quellen-Tracks werden die Items gescannt:
  - `min(Item-Start)` → Beginn der Region
  - `max(Item-Ende)`  → Ende der Region
- Das Script legt eine Region fest von:
  - `ts_start = min_start`
  - `ts_end   = max_end + TAIL_SECONDS`

`TAIL_SECONDS` ist im Script konfigurierbar (Standard: 0.5 s).

### 3. Zustände sichern

- Aktuelle Time Selection wird gespeichert.
- Aktuelle Cursorposition wird gespeichert.

### 4. OneClickReamp (V79) ausführen

- `DF95_V79_ReampSuite_OneClickReamp.lua` wird via `dofile` aufgerufen.
- Dieses Script:
  - nutzt PedalChains Intelligence 2.0 (falls vorhanden)
  - setzt `DF95_REAMP/TRACK_IDS`
  - ruft `DF95_ReampSuite_Router.lua` auf
  - erzeugt ReampReturn-Tracks
  - richtet das Hardware-Routing ein

### 5. ReampReturn-Tracks einsammeln

- Danach werden alle Tracks im Projekt gescannt.
- Alle Tracks, deren Name `ReampReturn` enthält (oder mit `ReampReturn_` beginnt),
  werden als ReampReturn-Tracks gespeichert.

Diese werden für die Post-Processing-Schritte (AutoOffset/AutoGain) selektiert.

### 6. Time Selection & Cursor setzen

- Die Time Selection wird auf `[ts_start, ts_end]` gesetzt.
- Der Cursor wird auf `ts_start` gesetzt.

### 7. Aufnahme

- Das Script startet einen `reaper.defer`-Loop (`session_loop`):
  - beim ersten Durchlauf wird `Transport: Record` gestartet
    (`Main_OnCommand(1013, 0)`).
  - anschließend wird in jeder Iteration folgendes geprüft:
    - Ist noch Recording aktiv (`GetPlayState() & 4 ~= 0`)?
    - Ist die aktuelle Position (`GetPlayPosition()`) >= `ts_end`?
  - Wenn das Ende erreicht ist, wird `Transport: Record` erneut aufgerufen,
    um die Aufnahme zu stoppen.

- Falls der User manuell die Aufnahme stoppt, erkennt der Loop dies ebenfalls
  und beendet die Session.

### 8. Nachbearbeitung (optional)

- Wenn `RUN_LATENCY_AUTOAPPLY = true` (Standard):

  ```lua
  dofile(df95_root() .. "ReampSuite/DF95_ReampSuite_ApplyLatencyOffset.lua")
  ```

  - Das Script verschiebt die Items auf den ReampReturn-Tracks anhand
    der gespeicherten `OFFSET_SAMPLES_<PROFILE>`-Werte.

- Wenn `RUN_AUTOGAIN_AFTER = true`:

  ```lua
  dofile(df95_root() .. "ReampSuite/DF95_ReampSuite_AutoGain.lua")
  ```

  - Das Script analysiert die ReampReturn-Pegel und schreibt
    `OUT_GAIN_DB_<PROFILE>` in `DF95_REAMP` (und optional Track-Volumes).

- Zur Sicherheit werden Fehler beim Ausführen dieser Scripts abgefangen
  und als MessageBox angezeigt.

### 9. Wiederherstellung

- Ursprüngliche Time Selection wird wiederhergestellt.
- Cursorposition wird wiederhergestellt.

---

## Konfiguration

Im Kopf des Scripts:

```lua
local TAIL_SECONDS = 0.5
local RUN_LATENCY_AUTOAPPLY = true
local RUN_AUTOGAIN_AFTER = false
```

- `TAIL_SECONDS`  
  - Steuert, wie viel "Nachklang" nach Ende der DI-Region noch aufgenommen wird.

- `RUN_LATENCY_AUTOAPPLY`  
  - `true`: Nach der Aufnahme wird automatisch der Latenz-Offset angewendet.
  - `false`: Kein AutoOffset – du kannst `DF95_ReampSuite_ApplyLatencyOffset` manuell ausführen.

- `RUN_AUTOGAIN_AFTER`  
  - `false` (Standard): AutoGain wird nicht automatisch ausgeführt.
  - `true`: AutoGain wird am Ende der Session gestartet.
  - Empfehlung: `true` verwenden, wenn du bewusst eine Kalibrierungs-Session
    fährst; `false` im täglichen Work-Flow.

---

## Installation

1. Dateien kopieren nach:

   - `Scripts/IFLS/DF95/ReampSuite/DF95_V80_ReampSuite_AutoSession.lua`
   - `Documentation/DF95_V80_ReampSuite_AutoSession.md` (optional)

2. In REAPER:

   - `Actions → Show action list…`
   - `New Action… → Load ReaScript…`
   - `DF95_V80_ReampSuite_AutoSession.lua` auswählen
   - Action registrieren

3. Optional in die ReampSuite-/Dashboard-Toolbar einbauen:

   - Label: `V80 AutoSession`
   - Action: `DF95_V80_ReampSuite_AutoSession`

---

## Typischer Workflow mit V80

1. **Setup (einmalig)**

   - Profil im ReampSuite Router wählen.
   - Optional: Latenz (Offset) und AutoGain für das Profil kalibrieren.

2. **Session**

   - DI-/Reamp-Quellen-Tracks selektieren (mit Items).
   - `V80 AutoSession` ausführen.
   - Das System richtet Routing + ReampReturn ein, setzt die Time Selection,
     startet die Aufnahme und stoppt automatisch am Ende.

3. **Nach der Session**

   - Items auf ReampReturn-Tracks sind (bei aktivierter Option)
     bereits zeitlich justiert (Offset) und ggf. zur Kalibrierung
     in AutoGain ausgewertet.
   - Du kannst nun wie gewohnt mit SuperPipeline/ExportDesk weiterarbeiten.

---

Mit DF95 V80 AutoSession hast du jetzt einen nahezu vollautomatisierten
Reamp-Prozess: Quellen wählen, Script starten – der Rest passiert für dich 🚀
