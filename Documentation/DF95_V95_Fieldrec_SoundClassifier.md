# DF95 V95 – Fieldrec SoundClassifier (Heuristic)

Dieses Modul ergänzt DF95/V90 um eine regelbasierte (nicht-KI) Klassifikation von Fieldrec-/PolyWAV-Material:

## Scripts

- **DF95_V95_Fieldrec_ItemAnalyze_Color.lua**
  - Analysiert selektierte Items.
  - Bestimmt eine dominante Klasse je Item:
    - LOW_PERC, SNARE_PERC, HAT/CYMBAL, DRONE/TEXTURE, FX/NOISE.
  - Färbt das Item passend ein.
  - Hängt ein Tag wie `[V95_LOW_PERC]` an den Item/Take-Namen an.

- **DF95_V95_Fieldrec_Split_And_Distribute.lua**
  - Segmentiert selektierte Items (Envelope-basierte Aktivitätserkennung).
  - Klassifiziert jedes Segment in eine der o.g. Klassen.
  - Erzeugt pro Klasse bei Bedarf einen Track:
    - V95_LOW_PERC, V95_SNARE_PERC, V95_HAT_CYMBAL, V95_DRONE_TEXTURE, V95_FX_NOISE.
  - Legt pro Segment ein neues Item auf dem passenden Klassentrack an (mit korrektem Source-Offset).

Beide Scripts arbeiten heuristisch auf Basis von:
- RMS-Hüllkurve / Aktivitätserkennung.
- FFT-Bandanalyse (Low / LowMid / Mid / High / Air).
