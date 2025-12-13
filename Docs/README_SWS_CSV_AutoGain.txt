DF95_LUFS_AutoGain_FromSWS_CSV.lua:
- sucht im Projektordner nach neuesten SWS-Loudness-CSV-Dateien
- mappt Track-/Item-Namen auf LUFS-I
- Ziel-LUFS: Track-ExtState DF95_META_lufs_target > Track-Notes lufs_target=… > Chain-ExtState > Default -14 LUFS
- clamp gem. Data/DF95/DF95_Humanize_Config.json
- Report in Data/DF95/Reports/AutoGain_YYYYMMDD_HHMMSS.txt
