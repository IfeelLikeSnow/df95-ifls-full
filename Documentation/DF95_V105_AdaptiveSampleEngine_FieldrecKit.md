# DF95 V105 – Adaptive Sample Engine (Fieldrec Kit)

V105 führt eine Adaptive Sample Engine für Fieldrec-basierte Kits ein.

## Ziel

- Situationen abfangen, in denen:
  - nur wenige Kicks/Snares/Hats vorhanden sind,
  - bestimmte Kategorien komplett fehlen (z.B. keine Snare),
  - Material gemischt ist, aber du trotzdem einen Artist-/Euclid-Beat
    generieren möchtest.
- Statt "Fehler" oder "Stille" berechnet V105:
  - Fallbacks (z.B. Snare aus Perc oder Hat),
  - "virtuelle Duplikate" (z.B. 1 Kick -> rechnerisch 4 Varianten),
  - und speichert eine Zusammenfassung in Project-ExtStates,
    so dass BeatEngines darauf reagieren können.

## Script

- `Scripts/IFLS/DF95/ReampSuite/DF95_V105_AdaptiveSampleEngine_FieldrecKit.lua`

## Funktionsweise

### 1. Basis: selektierte Items

- Du selektierst alle Slices/Samples, die als Pool dienen sollen:
  - typischerweise Output von V95/V95.2 (Fieldrec-Slicer/Classifier),
  - oder Items auf einem Kit-Track.
- V105 analysiert ausschließlich die **selektierten Media Items**.

### 2. Kategorisierung

Für jedes Item:

- Versucht V105, die Kategorie zu bestimmen:
  - Item-Notes (falls vorhanden, z.B. von V95):
    - `[KICK]`, `[SNARE]`, `[HAT]`, `class:kick`, `class:snare`, etc.
  - Take-Name + Track-Name:
    - enthält z.B. "kick", "bd", "snare", "hat", "hh", "tom", "perc", "clap" etc.

Die Items werden in folgende Kategorien einsortiert:

- KICK
- SNARE
- HAT
- PERC
- OTHER

### 3. Zielgrößen und Fallbacks

V105 hat intern Zielgrößen:

- KICK: 4
- SNARE: 6
- HAT: 8
- PERC: 4

Für jede Kategorie wird geprüft:

- Wie viele reale Slices existieren?
- Wenn 0 → Fallback-Kategorie setzen
  - z.B. SNARE -> PERC -> HAT -> OTHER
  - KICK -> PERC -> OTHER
  - HAT -> PERC -> OTHER
- Wenn weniger als Zielgröße → virtuelle Duplikate berechnen
  - z.B. 1 Kick -> 3 virtuelle Duplikate = 4 Varianten insgesamt.

### 4. Speicherung in Project-ExtStates

Alle Ergebnisse werden unter `DF95_ADAPTIVE` gespeichert:

Counts:

- `DF95_ADAPTIVE/KICK_REAL_COUNT`
- `DF95_ADAPTIVE/SNARE_REAL_COUNT`
- `DF95_ADAPTIVE/HAT_REAL_COUNT`
- `DF95_ADAPTIVE/PERC_REAL_COUNT`
- `DF95_ADAPTIVE/OTHER_COUNT`

Pools (GUID-Listen der Items, getrennt durch `;`):

- `DF95_ADAPTIVE/KICK_GUIDS`
- `DF95_ADAPTIVE/SNARE_GUIDS`
- `DF95_ADAPTIVE/HAT_GUIDS`
- `DF95_ADAPTIVE/PERC_GUIDS`
- `DF95_ADAPTIVE/OTHER_GUIDS`

Fallbacks:

- `DF95_ADAPTIVE/KICK_FALLBACK`
- `DF95_ADAPTIVE/SNARE_FALLBACK`
- `DF95_ADAPTIVE/HAT_FALLBACK`
- `DF95_ADAPTIVE/PERC_FALLBACK`

Virtuelle Duplikate:

- `DF95_ADAPTIVE/KICK_VIRTUAL_COUNT`
- `DF95_ADAPTIVE/SNARE_VIRTUAL_COUNT`
- `DF95_ADAPTIVE/HAT_VIRTUAL_COUNT`
- `DF95_ADAPTIVE/PERC_VIRTUAL_COUNT`

### 5. Anzeige

Nach der Analyse zeigt V105 eine Zusammenfassung an, z.B.:

- KICK: 1 (Fallback: PERC, virtuelle Duplikate: 3)
- SNARE: 0 (Fallback: HAT, virtuelle Duplikate: 6)
- HAT:   5 (Fallback: none, virtuelle Duplikate: 3)
- PERC:  2 (Fallback: OTHER, virtuelle Duplikate: 2)
- OTHER: 7

### 6. Nutzung in Kombination mit BeatEngines

Aktuell (Stand V105):

- V105 selbst erzeugt keine MIDI-Beats.
- Die Informationen in `DF95_ADAPTIVE/*` können aber von:

  - V102 Artist+Style BeatEngine,
  - V104 Euclid-MultiLane,
  - künftigen Scripts (z.B. V106+)

genutzt werden, um:

- bei fehlender Snare:
  - die Snare-Spur z.B. mit Perc/hat-Fallback zu belegen,
- bei zu wenig Kicks:
  - denselben Kick mehrfach mit leichten Variationen zu verwenden,
- bei reinen Hat-Sets:
  - Artist-/Euclid-Beats trotzdem sinnvoll aufzubauen.

## Typischer Workflow mit V105

1. Fieldrec aufnehmen, Slices mit V95/V95.2 erstellen (inkl. Klassifizierung, falls aktiv).
2. Alle relevanten Slices selektieren.
3. Script `DF95_V105_AdaptiveSampleEngine_FieldrecKit.lua` ausführen.
4. Meldung prüfen (wie viele Kicks/Snares/Hats vorhanden, Fallbacks etc.).
5. Danach V102/V104 nutzen, um Artist-/Euclid-Beats zu erzeugen – mit dem Wissen,
   dass das Projekt über `DF95_ADAPTIVE/*` eine saubere Beschreibung des
   verfügbaren Sample-Pools bereitstellt.

