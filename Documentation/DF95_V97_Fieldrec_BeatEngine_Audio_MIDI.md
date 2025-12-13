# DF95 V97 – Fieldrec BeatEngine (Audio & MIDI)

V97 baut auf den V95/V95.1-Fieldrec-Tools auf und erzeugt daraus Beats – sowohl direkt mit Audio-Slices als auch als MIDI-Pattern für Sampler.

## Voraussetzungen

- Du hast dein Fieldrec-/PolyWAV-Material mit den V95-Scripts bearbeitet:
  - `DF95_V95_Fieldrec_Split_And_Distribute.lua`
  - oder `DF95_V95_1_Fieldrec_Split_And_Distribute_MicBundle_AutoGain.lua`
- Dadurch existieren im Projekt Tracks der Form:
  - `V95_LOW_PERC*`   (Kick/Tom-Rolle)
  - `V95_SNARE_PERC*` (Snare-Rolle)
  - `V95_HAT_CYMBAL*` (HiHat/Cymbal-Rolle)

## Scripts

### 1. DF95_V97_Fieldrec_BeatEngine_Audio.lua

- Sucht in der Session nach V95-Klassentracks und sammelt die Items der Rollen:
  - LOW_PERC   -> Kick
  - SNARE_PERC -> Snare
  - HAT_CYMBAL -> Hat
- Fragt nach:
  - Beat-Style:
    - 1 = Basic (4/4 Backbeat, 8tel-Hats)
    - 2 = Tegra-ish (leichte Synkopen, dichter)
    - 3 = Squarepusher-ish (dichtere 16tel-Hats, randomisiert)
  - Bars (Anzahl Takte).
- Erzeugt einen Folder `V97_Beat_Audio` mit Child-Tracks:
  - `V97_Kick_Audio`
  - `V97_Snare_Audio`
  - `V97_Hat_Audio`
- Platziert pro Rolle Kopien der V95-Slices auf diesen Tracks:
  - Zeitposition nach Pattern
  - Slice-Auswahl per Zufall aus den vorhandenen Hits
  - kleine Safety-Fades an den Segment-Items

### 2. DF95_V97_Fieldrec_BeatEngine_MIDI.lua

- Nutzt dieselben Beat-Styles wie die Audio-Variante.
- Erzeugt einen neuen Track `V97_Beat_MIDI` mit einem MIDI-Item über die gewünschte Anzahl Takte.
- Schreibt ein Drum-Pattern nach GM-Standard:
  - Kick  = Note 36
  - Snare = Note 38
  - Hat   = Note 42
- Die MIDI-Daten können auf beliebige Sampler/Drumracks geroutet werden – z.B. auf Instrumente, die aus deinen V95-Slices gebaut wurden.

## Typischer Workflow

1. Fieldrec importieren (ggf. PolyWAV zunächst in Monotracks explodieren).
2. V95/V95.1 einsetzen:
   - Items analysieren, splitten und nach Klassen/Foldern verteilen.
3. V97 Audio- oder MIDI-Engine starten:
   - `DF95_V97_Fieldrec_BeatEngine_Audio.lua` für direktes Arbeiten mit Audio-Slices.
   - `DF95_V97_Fieldrec_BeatEngine_MIDI.lua` für Sampler-basierte Beats.
4. Optional:
   - V97-MIDI-Track auf einen Sampler routen, der deine V95-Slices als Kit lädt.
