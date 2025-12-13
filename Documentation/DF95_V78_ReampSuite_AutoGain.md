
# DF95 V78 – ReampSuite AutoGain

Dieses Add-on ergänzt dein DF95-/ReampSuite-Setup um ein Script, das
die Pegel deiner ReampReturn-Tracks analysiert und daraus einen
Gain-Offset für dein aktuelles Reamp-Profil berechnet.

Ziel: eine reproduzierbare, kalibrierte Reamp-Lautstärke pro Profil.

---

## Inhalt

- `Scripts/IFLS/DF95/ReampSuite/DF95_ReampSuite_AutoGain.lua`  
  Script, das:

  - das aktive Reamp-Profil aus `DF95_ReampSuite_Profiles.lua` liest
  - ReampReturn-Tracks analysiert (Peak in dBFS)
  - einen Gain-Offset berechnet, um einen Ziel-Peak (z. B. -12 dBFS) zu erreichen
  - den Wert in `DF95_REAMP/OUT_GAIN_DB_<PROFILE_KEY>` speichert
  - optional diesen Gain direkt auf Track-Volumes anwendet

- `Documentation/DF95_V78_ReampSuite_AutoGain.md`  
  Diese Datei.

---

## Voraussetzungen

- DF95 ReampSuite ist installiert (inkl. `DF95_ReampSuite_Profiles.lua`).
- Du hast bereits mit deinem Profil Reamp-Aufnahmen gemacht, z. B.:
  - per `DF95_V76_SuperPipeline.lua`
  - oder manuell über `DF95_ReampSuite_Router.lua`

- Die ReampReturn-Tracks heißen idealerweise `ReampReturn_<irgendwas>`,
  damit sie automatisch erkannt werden, falls du keine Tracks selektierst.

---

## Funktionsweise

1. Script lädt `DF95_ReampSuite_Profiles.lua` und ermittelt das aktive Profil
   über `get_active_key()` (z. B. `UR22_DI_Pedals`).

2. Ziel-Tracks:

   - Wenn **Tracks selektiert** sind:
     - Es werden **genau diese** Tracks analysiert.
   - Wenn **keine Tracks selektiert** sind:
     - Es werden alle Tracks verwendet, deren Name `ReampReturn` enthält.

3. Pro Track werden alle Items (aktiver Take) über
   `GetMediaItemTake_Peaks(...)` gescannt und der **maximale Peak**
   (Betragswert, 0..1) ermittelt.

4. Der globale Maximal-Peak wird in dBFS umgerechnet:

   ```text
   current_peak_db = 20 * log10(global_peak)
   ```

5. Der Gain-Offset wird berechnet als:

   ```text
   gain_db = TARGET_PEAK_DB - current_peak_db
   ```

   Dabei ist `TARGET_PEAK_DB` im Script einstellbar (Standard: -12 dBFS).
   Zur Sicherheit wird der Wert auf ±24 dB begrenzt.

6. Der Gain-Offset wird gespeichert in:

   ```text
   Namespace: DF95_REAMP
   Key:       OUT_GAIN_DB_<PROFILE_KEY>
   Beispiel:  OUT_GAIN_DB_UR22_DI_Pedals = -3.50
   ```

7. Optional (steuerbar über `APPLY_GAIN_TO_TRACKS` im Script):

   - Der berechnete Gain wird direkt auf die Track-Volumes angewendet
     (`D_VOL` pro Track).  
   - Standard: `false` – sprich: nur Messung + Speichern.

8. Am Ende zeigt das Script eine Zusammenfassung (Profil, Peaks, Gain, Anzahl Tracks/Items).

---

## Verwendung (empfohlener Kalibrierungs-Workflow)

1. **Profil wählen**
   - `DF95_ReampSuite_Router` öffnen und ein Profil wählen (z. B. UR22_DI_Pedals).
   - Sicherstellen, dass das Routing für Reamp richtig funktioniert.

2. **Referenz-Reamp aufnehmen**
   - Ein geeignetes Referenzsignal reampen:
     - z. B. eine DI-Gitarre, ein Percussion-Loop oder ein Test-Loop.
   - Die ReampReturn-Spuren sollten nun ein repräsentatives Signal enthalten.

3. **AutoGain ausführen**
   - ReampReturn-Tracks selektieren (oder unselektiert lassen, wenn sie `ReampReturn` heißen).
   - `DF95_ReampSuite_AutoGain` ausführen.
   - Im Dialog siehst du:
     - globalen Peak in dBFS
     - Ziel-Peak
     - berechneten Gain-Offset
     - den ExtState-Key, in dem der Wert gespeichert wurde.

4. **Optionale direkte Gain-Anwendung**
   - Wenn du möchtest, dass der Gain sofort als Track-Volume angewendet wird:
     - Setze im Script `APPLY_GAIN_TO_TRACKS = true`.
     - Erneut ausführen.
   - Ansonsten dient der Wert vor allem als Kalibrierungs-Referenz für zukünftige Reamps.

5. **Zukünftige Integration in Router (optional)**
   - Ein späteres Update (oder manueller Patch) im `DF95_ReampSuite_Router.lua`
     kann `OUT_GAIN_DB_<PROFILE>` aus `DF95_REAMP` lesen und z. B. den
     Send-Gain oder einen Trim in der Reamp-Kette automatisch setzen.

---

## Konfiguration

Im Kopf des Scripts findest du:

```lua
local TARGET_PEAK_DB = -12.0       -- Ziel-Peak in dBFS
local MAX_ABS_GAIN_DB = 24.0       -- maximale Korrektur in dB
local APPLY_GAIN_TO_TRACKS = false -- Track-Volumes automatisch anpassen?
```

- `TARGET_PEAK_DB`:
  - typischer Wert: `-12.0` oder `-18.0`
  - hängt von deiner gewünschten Reamp-Headroom-Philosophie ab.

- `MAX_ABS_GAIN_DB`:
  - Schutz, damit keine absurden Korrekturen stattfinden.

- `APPLY_GAIN_TO_TRACKS`:
  - `false`: Script schreibt nur den ExtState, ändert aber keine Track-Volumes.
  - `true`: zusätzlich werden die Track-Volumes entsprechend angepasst.

---

## Hinweise

- Das Script verändert nur:
  - ggf. die `D_VOL`-Werte der Ziel-Tracks (wenn `APPLY_GAIN_TO_TRACKS = true`)
  - und setzt `DF95_REAMP/OUT_GAIN_DB_<PROFILE_KEY>`.

- Es werden keine Items, FX oder Sends gelöscht oder neu erzeugt.

- Alles läuft in einem Undo-Block und kann rückgängig gemacht werden.

---

Mit diesem AutoGain-Add-on hast du jetzt pro Profil eine
skalierbare, reproduzierbare Reamp-Lautstärke – perfekt passend zu
deinem V76.2-Latenz-Align und dem V77 Dashboard 🚀
