
# DF95 Drone Harmonization – Phase L

Diese Phase stellt **kanonische Enums und Normalisierungsfunktionen** für alle Drone-bezogenen Felder bereit:

- `df95_drone_centerfreq`
- `df95_drone_density`
- `df95_drone_form`
- `df95_drone_motion` / `df95_motion_strength`
- `df95_tension`

## 1. Canonical Sets

Empfohlene, systemweit einheitliche Werte:

```lua
centerfreq: LOW, MID, HIGH
density:    LOW, MED, HIGH
form:       PAD, TEXTURE, SWELL, MOVEMENT, GROWL
motion:     STATIC, MOVEMENT, PULSE, SWELL
tension:    LOW, MED, HIGH, EXTREME
```

Diese sind in `DF95_Drone_Enums_PhaseL.lua` definiert.

## 2. Integration in AutoIngest (Phase G)

In `DF95_AutoIngest_Master_V4.lua`:

1. Oben (nach `local r = reaper` o.ä.):

```lua
local DF95_DroneEnums = dofile(reaper.GetResourcePath()
  .. "/Scripts/IFLS/DF95/DF95_Drone_Enums_PhaseL.lua")
```

2. In `analyze_drone_audio(it)` sicherstellen, dass zurückgelieferte Werte **die kanonischen Enums** nutzen, z. B.:

```lua
dx.centerfreq = DF95_DroneEnums.normalize_centerfreq(raw_centerfreq)
dx.density    = DF95_DroneEnums.normalize_density(raw_density)
dx.form       = DF95_DroneEnums.normalize_form(raw_form)
dx.motion     = DF95_DroneEnums.normalize_motion(raw_motion)
dx.tension    = DF95_DroneEnums.normalize_tension(raw_tension)
```

3. Vor dem Writeback im AutoIngest-Loop optional:

```lua
DF95_DroneEnums.normalize_item_drone_fields(it)
```

## 3. Integration in Inspector V5

In `DF95_SampleDB_Inspector_V5_AI_Review_ImGui.lua`:

- beim Einlesen eines Items (oder direkt in `item_matches_filters(it)`) kannst du sicherstellen:

```lua
local enums = DF95_DroneEnums
local cf   = enums.normalize_centerfreq(it.df95_drone_centerfreq)
local dens = enums.normalize_density(it.df95_drone_density)
local form = enums.normalize_form(it.df95_drone_form)
local mot  = enums.normalize_motion(it.df95_motion_strength or it.df95_drone_motion)
local ten  = enums.normalize_tension(it.df95_tension)
```

Dann mit diesen normalisierten Werten gegen die Filter vergleichen.

## 4. Integration in Analyzer & Dashboard

Im Analyzer und im Drone Dashboard musst du typischerweise nur lesen; trotzdem kannst du vor der Statistikbildung:

```lua
DF95_DroneEnums.normalize_item_drone_fields(it)
```

aufrufen, damit alte Werte (`MEDIUM`, `TENSE`, etc.) konsistent in die gleichen Buckets fallen.

## 5. Integration in PackExporter

Im PackExporter-Skript kannst du beim Filtern:

- entweder direkt mit `DF95_DroneEnums.normalize_*` arbeiten,
- oder beim Einlesen der Items `normalize_item_drone_fields()` aufrufen.

## 6. Migration älterer Einträge (optional)

Falls in deiner DB schon viele ältere Werte stecken (z. B. `MEDIUM`, `STATIC_PAD`, `LOWCF` etc.), kannst du ein einfaches Migrationsskript schreiben:

```lua
local enums = DF95_DroneEnums
for _, it in ipairs(db.items or {}) do
  enums.normalize_item_drone_fields(it)
end
-- danach DB zurückschreiben
```

Das bringt deine komplette Library auf einen konsistenten Stand.

---

Wenn alle relevanten Skripte diese Enums-/Normalization-Schicht verwenden, sind alle Drone-Funktionen (AutoIngest, Inspector, Analyzer, Dashboard, PackExporter) harmonisiert und robust gegenüber alten Varianten.
