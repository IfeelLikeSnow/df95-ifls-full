# DF95 Chain Naming Policy (Mic / FXBus / Coloring / Master)

Ziel dieser Policy:

- Autopilot/Artist-Skripte bleiben kompatibel.
- Künftige Erweiterungen (Zoom F6/H5, Android, Reamp) können sauber andocken.
- Toolbars & Dropdown-Menüs können Chains logisch gruppieren.
- Chains sind leichter wartbar und dokumentierbar.

## Grundregeln

- Ordnerstruktur bleibt unverändert (Mic, FXBus, Coloring, Master, Artists, Styles).
- Präfixe pro Typ bleiben erhalten:
  - Mic-Chains: `Mic_`
  - FXBus-Chains: `FXBus_` oder `DF95_FXBus_`
  - Coloring-Chains: `Color_`
  - Master-Chains: `Master_`

Scripts erkennen Chains anhand dieser Präfixe + Ordnerpfade.

## Mic-Chains

Pfad: `FXChains/DF95/Mic/…`

Empfohlenes Schema:

`Mic_[Recorder?]_[Model]_[Pattern?]_[Mono|Stereo].RfxChain`

Beispiele:

- Mic_MD400_Mono.RfxChain
- Mic_ZF6_MD400_Mono.RfxChain
- Mic_Android_FieldRec_Wide_Stereo.RfxChain

Pflicht:

- `Mic_` Präfix
- eindeutiger Modell-/Typname
- `Mono` oder `Stereo` im Namen

## FXBus-Chains

Pfad: `FXChains/DF95/FXBus/…`

Empfohlenes Schema:

`DF95_FXBus_[Character]_[Tags...]_[Safe?].RfxChain`

Tags können sein: `_Safe`, `_FULL`, `_LIVE`, `_EXTREME` usw.

## Coloring-Chains

Pfad: `FXChains/DF95/Coloring/…`

Schema:

`Color_[Style]_[Character]_[Engine].RfxChain`

Artist-Chains bleiben unter `FXChains/DF95/Coloring/Artists/<Artist>/`.

## Master-Chains

Pfad: `FXChains/DF95/Master/…`

Schema:

`Master_[Style]_[Character]_[Tags].RfxChain`

Optional können LUFS-Targets hinzugefügt werden, z. B.:

- Master_Neutral_-14LUFS_Streaming.RfxChain
- Master_Neutral_-23LUFS_TVFilm.RfxChain

## Safe vs. Risky Renames

SICHER:

- Inhaltliche Änderungen einer Chain (FX, Gain, Reihenfolge).
- Hinzufügen von Recorder-/Pattern-Tags HINTER dem bestehenden Präfix.
- Hinzufügen von `_Safe`, `_FULL`, `_LIVE`, `_EXTREME`, `-14LUFS_Streaming` usw.
- Vereinheitlichung der Dateiendung auf `.RfxChain`.

RISKANT:

- Entfernen von `Mic_`, `Color_`, `FXBus_`, `Master_`.
- Umbenennen von Künstler-Ordnern unter `Coloring/Artists/`.
- Umbenennen oder Verschieben von Style-/Kategorieordnern, wenn Scripts diese nutzen.

Details siehe auch DF95 Installer / Autopilot Dokumente.
