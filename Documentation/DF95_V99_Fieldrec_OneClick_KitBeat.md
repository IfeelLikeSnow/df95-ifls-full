# DF95 V99 – OneClick Fieldrec → Kit → Beat

V99 ist eine OneClick-Pipeline, die mehrere DF95-Module verknüpft:

- V95.2 Fieldrec SplitEngine
- V98 SliceKit Builder (RS5k)
- V97 BeatEngine MIDI

Ziel: Aus rohen Fieldrec-Items mit einem einzigen Script-Aufruf einen spielbaren Beat
mit eigenem SliceKit zu erzeugen.

## Script: DF95_V99_Fieldrec_OneClick_KitBeat.lua

### Ablauf

1. Erwartet selektierte Fieldrec-Items (Audio, kein MIDI).
2. Ruft `DF95_V95_2_Fieldrec_OneClick_SplitEngine.lua` auf:
   - Single-Mic vs. Multi-Mic (MicBundle) wird automatisch erkannt.
   - V95/V95.1 erzeugen Klassentracks:
     - `V95_LOW_PERC*`
     - `V95_SNARE_PERC*`
     - `V95_HAT_CYMBAL*`
     - usw.
3. Ruft `DF95_V98_Fieldrec_SliceKitBuilder_RS5k.lua` auf:
   - Erzeugt einen Track `V98_SliceKit_RS5k`.
   - Baut pro Rolle eine ReaSamplomatic5000-Instanz:
     - LOW_PERC   → Note 36 (Kick)
     - SNARE_PERC → Note 38 (Snare)
     - HAT_CYMBAL → Note 42 (Hat)
4. Ruft `DF95_V97_Fieldrec_BeatEngine_MIDI.lua` auf:
   - Erzeugt Track `V97_Beat_MIDI`.
   - Fragt nach Beat-Style (Basic/Tegra/Squarepusher) und Anzahl Takte.
5. Verbindet `V97_Beat_MIDI` automatisch mit `V98_SliceKit_RS5k` via MIDI-Send:
   - Audio-Send wird deaktiviert (nur MIDI).
   - Der Kit-Track gibt Audio aus.

### Verwendung

1. Fieldrec-/PolyWAV-Material ins Projekt laden.
2. Ggf. PolyWAV in Monotracks explodieren (für MicBundles).
3. Relevante Fieldrec-Items selektieren.
4. `DF95_V99_Fieldrec_OneClick_KitBeat` ausführen.
5. Ergebnis:
   - Slices/Klassentracks (V95/V95.1),
   - RS5k-SliceKit (V98),
   - MIDI-Beat (V97),
   - Routing zwischen Beat-Track und Kit-Track.

Danach kannst du:
- das MIDI-Pattern editieren,
- RS5k-Settings feinjustieren,
- zusätzliche FX auf dem Kit-Track oder den V95-Klassentracks verwenden.
