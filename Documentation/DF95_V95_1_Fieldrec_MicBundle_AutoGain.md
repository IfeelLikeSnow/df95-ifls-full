# DF95 V95.1 – Fieldrec MicBundle Split & Distribute (Folder + AutoGain)

Dieses Script erweitert den V95-Fieldrec-Classifier um MicBundle- und Folder-Funktionalität:

## Ziel

Multimikro-Aufnahmen (z.B. Zoom H5/H6/F6 oder Mehrkanal-Sessions) sollen als „Bundle“ bearbeitet werden, sodass:

- alle Mics gemeinsam segmentiert werden,
- jedes Segment einer Klasse zugeordnet wird (LOW_PERC, SNARE_PERC, HAT/CYMBAL, DRONE/TEXTURE, FX/NOISE),
- pro Klasse ein Folder-Master entsteht,
- pro Mic Child-Tracks unter diesem Master angelegt werden,
- die Items pro Mic/Segment automatisch auf die passenden Child-Tracks gelegt werden,
- ein einfaches AutoGain pro Child-Track durchgeführt wird.

## Workflow

1. Alle Items, die zu einer Multimikro-Aufnahme gehören, selektieren (z.B. 3 Spuren einer H5-Aufnahme).
2. Script ausführen:
   - `DF95_V95_1_Fieldrec_Split_And_Distribute_MicBundle_AutoGain`.
3. Ergebnis im Projekt:
   - Folder pro Klasse, z.B.:
     - V95_LOW_PERC
     - V95_SNARE_PERC
     - V95_HAT_CYMBAL
     - V95_DRONE_TEXTURE
     - V95_FX_NOISE
   - Darunter Child-Tracks pro Mic:
     - V95_SNARE_PERC_Mic1, V95_SNARE_PERC_Mic2, V95_SNARE_PERC_Mic3, etc.
   - Segment-Items werden pro Mic zeitlich korrekt erzeugt und eingefärbt.
   - AutoGain skaliert die Item-Gains pro Child-Track so, dass der globale Peak bei ca. -6 dBFS liegt.

## Hinweise

- Track-Fader bleiben unberührt – sie bleiben vollständig zum Mischen verfügbar.
- Die Klassifikation basiert auf einem Referenz-Mic (erstes selektiertes Item) und nutzt:
  - FFT-Bandanalyse (Low / LowMid / Mid / High / Air).
  - Segmentdauer und spektrale Gewichtungen.
- Das Script ist für „ein Bundle pro Run“ gedacht: alle zugehörigen Mics gemeinsam selektieren, dann starten.
