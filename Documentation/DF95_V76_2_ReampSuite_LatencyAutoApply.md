
# DF95 V76.2 – ReampSuite Latency AutoApply

Dieses Add-on ergänzt dein bestehendes DF95-/ReampSuite-Setup um ein Script,
das die gemessene Reamp-Latenz automatisch auf deine ReampReturn-Items anwendet.

---

## Inhalt

- `Scripts/IFLS/DF95/ReampSuite/DF95_ReampSuite_ApplyLatencyOffset.lua`  
  Action, die:
  - das aktive Reamp-Profil ermittelt (über `DF95_ReampSuite_Profiles.lua`)
  - den dazugehörigen `OFFSET_SAMPLES_<PROFILE>`-Wert aus `DF95_REAMP` liest
  - ReampReturn-Tracks findet
  - alle Items auf diesen Tracks entsprechend verschiebt

- `Documentation/DF95_V76_2_ReampSuite_LatencyAutoApply.md`  
  Diese Datei.

---

## Voraussetzungen

- Dein DF95-ReampSuite-Setup ist bereits installiert (V71–V76 / V76.1).
- Du verwendest die Reamp-Profile aus `DF95_ReampSuite_Profiles.lua`.
- Du hast mit `DF95_V71_LatencyAnalyzer.lua` oder dem
  `DF95_ReampSuite_LatencyHelper.lua` einen Latenzwert gemessen und in
  `DF95_REAMP` gespeichert, z. B.:

  - Namespace: `DF95_REAMP`
  - Key: `OFFSET_SAMPLES_UR22_DI_Pedals`
  - Value: `128` (Samples)

---

## Funktionsweise

1. Das Script lädt `DF95_ReampSuite_Profiles.lua` und ermittelt den aktiven Profil-Key,
   z. B. `UR22_DI_Pedals`.

2. Es erwartet einen ExtState der Form:

   ```
   Namespace: DF95_REAMP
   Key:       OFFSET_SAMPLES_<PROFILE_KEY>
   Beispiel:  OFFSET_SAMPLES_UR22_DI_Pedals = 128
   ```

3. Ziel-Tracks:

   - Wenn **Tracks selektiert** sind:
     - Es werden **genau diese** Tracks als Ziel genommen.
   - Wenn **keine Tracks selektiert** sind:
     - Es werden alle Tracks verwendet, deren Name mit `ReampReturn_` beginnt
       oder `ReampReturn` im Namen enthält.

4. Alle Items auf diesen Ziel-Tracks werden um

   ```
   offset_sec = OFFSET_SAMPLES / Samplerate
   ```

   Sekunden nach vorne verschoben (d. h. zu früherem Zeitpunkt im Projekt).
   **Positive Werte bedeuten: Reamp-Signal kommt zu spät → wir ziehen es nach vorne.**

5. Item-Positionen, die unter 0 fallen würden, werden auf 0 geklemmt.

6. Am Ende zeigt das Script eine Zusammenfassung:

   - Aktives Profil
   - Offset in Samples
   - Anzahl betroffener Tracks
   - Anzahl verschobener Items

---

## Installation

1. Dieses Add-on **nicht** über dein gesamtes Repo „drüberkopieren“, sondern
   gezielt in deinen REAPER-ResourcePath kopieren:

   - `Scripts/IFLS/DF95/ReampSuite/DF95_ReampSuite_ApplyLatencyOffset.lua`
   - `Documentation/DF95_V76_2_ReampSuite_LatencyAutoApply.md` (optional)

2. In REAPER:

   - `Actions → Show action list…`
   - `New Action… → Load ReaScript…`
   - `DF95_ReampSuite_ApplyLatencyOffset.lua` auswählen
   - Action registrieren

3. Optional eine Toolbar-Button anlegen, z. B. in deiner ReampSuite-Toolbar:

   - Label: `Apply Reamp Offset`
   - Action: `DF95_ReampSuite_ApplyLatencyOffset`

---

## Typischer Workflow

1. **Einmal pro Setup / Profil:**

   - `DF95_ReampSuite_LatencyHelper` starten
   - Testimpuls aufnehmen
   - Latenz in Samples bestimmen (Differenz zwischen Original-Impuls und ReampReturn)
   - Wert als `OFFSET_SAMPLES_<PROFILE_KEY>` in `DF95_REAMP` speichern

2. **Im täglichen Reamp-Workflow:**

   - Reamp-Session wie gewohnt mit V76 (SuperPipeline + ReampSuite) durchführen
   - Wenn du zufrieden mit dem Take bist:
     - ReampReturn-Tracks selektieren (oder unselektiert lassen, wenn sie mit `ReampReturn_` heißen)
     - `DF95_ReampSuite_ApplyLatencyOffset` ausführen
   - Items werden entsprechend deines Offsets automatisch passend verschoben.

---

## Hinweise / Sicherheit

- Das Script verändert **nur die Item-Position** auf den Ziel-Tracks.
- Es werden keine Items gelöscht, keine Takes entfernt, keine FX geändert.
- Alles läuft in einem Undo-Block – du kannst die Änderung jederzeit mit `Ctrl+Z`
  rückgängig machen.

---

Viel Spaß mit deinem jetzt vollständig automatisierten Reamp-Flow:
Profil → Routing → PedalChain → Latenz-Align 🚀
