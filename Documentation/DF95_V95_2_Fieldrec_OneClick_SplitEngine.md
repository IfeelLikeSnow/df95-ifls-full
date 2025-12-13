# DF95 V95.2 – Fieldrec OneClick SplitEngine

Dieses Script ist ein Wrapper um die V95-Fieldrec-Tools und entscheidet automatisch,
welcher Split-Workflow passend ist:

- **Single-Mic-Case (alle selektierten Items auf einem Track):**
  - ruft `DF95_V95_Fieldrec_Split_And_Distribute.lua` auf.
  - Energy-basierte Segmentierung mit Safety-Fades an den neuen Items.

- **Multi-Mic-Case (selektierte Items auf mehreren Tracks):**
  - ruft `DF95_V95_1_Fieldrec_Split_And_Distribute_MicBundle_AutoGain.lua` auf.
  - Gemeinsame Segmentierung über alle Mics.
  - Folder-Master pro Klasse (LOW_PERC, SNARE_PERC, HAT/CYMBAL, DRONE/TEXTURE, FX/NOISE).
  - Child-Tracks pro Mic (z.B. V95_SNARE_PERC_Mic1..3).
  - AutoGain pro Child-Track (Peak ~ -6 dBFS) und Safety-Fades an den Segment-Items.

## Verwendung

1. Alle relevanten Fieldrec-/PolyWAV-Items selektieren (ein- oder mehrspurige Aufnahme).
2. `DF95_V95_2_Fieldrec_OneClick_SplitEngine` ausführen.
3. Je nach Situation wird automatisch der passende Workflow angewendet.

Dieses Script setzt voraus, dass die folgenden Scripts im selben Ordner liegen:

- `DF95_V95_Fieldrec_Split_And_Distribute.lua`
- `DF95_V95_1_Fieldrec_Split_And_Distribute_MicBundle_AutoGain.lua`
