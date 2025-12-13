# DF95 V107 – Fieldrec Adaptive BeatEngine (MIDI, Prototyp)

V107 ist die erste prototypische BeatEngine, die alle bisherigen Schichten
zusammenführt:

- Artist + Style (V102 / V103)
- Euclid Multi-Lane (V104)
- Adaptive Sample Engine (V105)
- Permission Layer (V106)

und daraus ein mehrtaktiges MIDI-Beatpattern erzeugt.

## Script

- `Scripts/IFLS/DF95/ReampSuite/DF95_V107_Fieldrec_AdaptiveBeatEngine_MIDI.lua`

## Überblick

V107:

1. liest Artist & Style aus Project-ExtStates:
   - `DF95_ARTIST/NAME`
   - `DF95_STYLE/NAME`

2. liest Adaptive Sample Info aus V105 (DF95_ADAPTIVE/*):
   - Real Counts, Fallbacks, virtuelle Duplikate.

3. liest Permission/Policy aus V106 (DF95_ADAPTIVE_CONFIG/*):
   - ob Kick/Snare/Hat rekonstruiert werden dürfen,
   - ob virtuelle Duplikate erlaubt sind,
   - ob Minimal- oder Full-Beat bevorzugt wird.

4. generiert ein mehrtaktiges Pattern für fünf Lanes:
   - Kick
   - Snare
   - Hat
   - Perc
   - Extra

   Die zeitliche Struktur basiert auf:
   - einem 4/4-Raster (standard), oder
   - optional der Euclid-Einstellung `DF95_EUCLID_MULTI/STEPS`
     (z.B. 7, 8, 12, 16 etc.).

5. optional: Euclid-Overlay auf KICK/SNARE/HAT/EXTRA:
   - liest `DF95_EUCLID_MULTI`:
     - `STEPS`, `DIVISION`
     - `KICK_PULSES`, `KICK_ROT`, `KICK_EN`
     - `SNARE_*`, `HAT_*`, `EXTRA_*`
   - legt ein Euclid-Pattern über das Artist-Pattern (logisches OR).

6. wendet den Mode-Filter an:
   - **Minimal Mode** (Standard, wenn V106 nichts anderes setzt):
     - Lanes ohne reale Samples (z.B. keine Kicks) werden komplett stumm geschaltet.
     - Kein Fallback, keine Rekonstruktion.
   - **Full Mode** (wenn `PREFER_FULL_BEAT = 1`):
     - Lanes ohne reale Samples können aktiv bleiben, wenn:
       - ein Fallback existiert (z.B. SNARE_FALLBACK = PERC),
       - und Rekonstruktion für diese Kategorie erlaubt ist
         (z.B. `ALLOW_RECONSTRUCT_SNARE = 1`).
     - Virtuelle Duplikate sind in diesem Prototyp nur als Info vorhanden
       (V107 nutzt sie noch nicht aktiv für Microvarianten).

7. schreibt das Ergebnis als MIDI-Item:
   - auf den zuerst selektierten Track,
   - oder, wenn kein Track selektiert ist, auf einen neu erstellten
     Track `DF95_V107_Beat`.

MIDI-Noten:

- Kick  = 36
- Snare = 38
- Hat   = 42
- Perc  = 39
- Extra = 40

Diese Noten können auf ein RS5k-SliceKit (z.B. aus V98) geroutet werden.

## Minimal vs. Full Mode

### Minimal Mode

- `DF95_ADAPTIVE_CONFIG/PREFER_MINIMAL_BEAT = 1`
- `PREFER_FULL_BEAT = 0`
- Rekonstruktions-Flags können 0 bleiben.

Verhalten:

- Für jede Lane wird geprüft, ob in der passenden Kategorie reale Samples existieren:
  - Kick-Lane → `KICK_REAL_COUNT > 0`
  - Snare-Lane → `SNARE_REAL_COUNT > 0`
  - Hat-Lane → `HAT_REAL_COUNT > 0`
  - Perc-/Extra-Lane → `PERC_REAL_COUNT > 0`

- Wenn `*_REAL_COUNT == 0`:
  - Lane wird komplett stumm geschaltet (Pattern->false).
  - Es werden keine Fallbacks genutzt.
  - Es werden keine künstlichen Kicks/Snares/Hats „erfunden“.

Damit gilt:

> Minimal Mode = Beat nur aus tatsächlich vorhandenen Sample-Kategorien.

### Full Mode

- `DF95_ADAPTIVE_CONFIG/PREFER_FULL_BEAT = 1`
- und/oder entsprechende `ALLOW_RECONSTRUCT_*` und `ALLOW_VIRTUAL_DUPES` sind gesetzt.

Verhalten:

- Wenn eine Kategorie keine realen Samples hat (`*_REAL_COUNT == 0`):
  - und Rekonstruktion für diese Kategorie erlaubt ist,
  - und ein Fallback existiert (z.B. SNARE_FALLBACK = PERC),
  - dann bleibt die Lane im Pattern aktiv.
  - (Die konkrete Sample-Zuweisung aus Fallback-Kategorien ist zukünftiges Feature.)

- In diesem Prototyp bedeutet Full-Mode vor allem:
  - Lanes können trotz fehlender Real-Samples im Pattern aktiv bleiben,
  - um in späteren Versionen (z.B. V108) mit Fallback-Samples befüllt zu werden.

## Euclid-Integration (optional)

Wenn `DF95_EUCLID_MULTI/STEPS > 0` gesetzt ist (z.B. durch V104 Panel):

- V107 setzt `steps_per_bar = STEPS`.
- Für KICK/SNARE/HAT/EXTRA werden Euclid-Muster generiert:
  - `*_PULSES`, `*_ROT`, `*_EN` werden berücksichtigt.
- Diese Muster werden über die Artist-Patterns gelegt (OR-Logik):
  - Wo Euclid `true` ist, wird die Lane im entsprechenden Step aktiv.

So kannst du z.B.:

- Artistspezifische Patterns + Euclid-Hats kombinieren,
- nur Euclid nutzen (Artist-Pattern sehr „dünn“ halten),
- ungerade Metriken (z.B. Steps=7, Pulses=3/4) ausprobieren.

## Workflow-Empfehlung

1. Fieldrec aufnehmen, slicen & klassifizieren (V95/V95.2).
2. Slices selektieren, `DF95_V105_AdaptiveSampleEngine_FieldrecKit.lua` ausführen.
3. `DF95_V106_AdaptiveBeat_PermissionPanel.lua` öffnen:
   - Minimal vs. Full einstellen,
   - Rekonstruktion & Virtuals erlauben oder verbieten.
4. (Optional) `DF95_V104_ArtistStyle_EuclidControlPanel_MultiLane.lua` öffnen:
   - Euclid-Pattern konfigurieren.
5. `DF95_V107_Fieldrec_AdaptiveBeatEngine_MIDI.lua` ausführen:
   - erzeugt ein MIDI-Beatpattern gemäß deiner Einstellungen.

## Status

V107 ist ein **Prototyp**:

- Die Verwendung von `DF95_ADAPTIVE/*` ist aktuell auf
  "Lane aktiv vs. stumm" beschränkt (insbesondere im Minimal-Mode).
- Fallbacks und virtuelle Duplikate werden bereits gelesen, aber noch nicht
  vollständig genutzt, um spezifische Sample-Auswahlen mit Microvarianten
  zu treffen – das ist für V108+ vorgesehen.
- Ziel war hier: ein hörbares, aber kontrollierbares System zu schaffen,
  das klar zwischen "nur vorhandenes Material" und "voller Artist-Beat
  mit Rekonstruktionsoption" unterscheidet.


## Update v1.2 – Anzahl Takte aus DF95_TIME/BARS

V107 liest jetzt zusätzlich `DF95_TIME/BARS` (gesetzt z.B. im V109 Meter Panel)
und erzeugt entsprechend viele Takte (Bars) im Beatpattern.
