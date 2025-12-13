\
# DF95 Drone System Consistency – Phase O (V2)

**Script:** `Scripts/IFLS/DF95/DF95_Drone_System_Consistency_PhaseO.lua`  
**Ziel:** Vollständiger Konsistenztest des Drone-Subsystems nach (oder auch vor) der Phase-N-Migration – inklusive optionaler Hooks zu QA (Phase J) und Dashboard/Inspector (Phase K).

---

## 1. Was ist neu in Phase O V2?

Phase O V1:

- prüft die SampleDB auf:
  - Vollständigkeit der Drone-Felder
  - Gültigkeit der Enum-Werte (Phase L)
  - einfache Plausibilität `df95_drone_motion` ↔ `df95_motion_strength`
- erzeugt einen Konsistenz-Report
- ist read-only (ändert die DB nicht)

**Phase O V2** baut darauf auf und ergänzt:

- eine **Konfigurationssektion (CFG)** für Subsystem-Hooks:
  - Phase J – Drone QA Validator
  - Dashboard-Drilldown-Test (Phase K)
  - Inspector-Test (Phase K)
- versucht, diese Actions über `reaper.NamedCommandLookup()` aufzurufen
- protokolliert den Status (enabled / found / ran / error) im Report und in der Konsole

Damit wird Phase O vom reinen DB-Checker zu einem **leichtgewichtigen Orchestrator** für dein Drone-QA-Ökosystem.

---

## 2. Konfiguration der Subsystem-Hooks (CFG)

Oben im Script findest du:

```lua
local CFG = {
  -- Phase J: Drone QA Validator
  enable_phaseJ       = false,
  phaseJ_cmd_str      = "", -- z.B. "_RSabcdef123456789"

  -- Dashboard Test (Phase K / Drilldown)
  enable_dashboard    = false,
  dashboard_cmd_str   = "", -- z.B. "_RS1234567890abcd"

  -- Inspector Test (Phase K / Inspector)
  enable_inspector    = false,
  inspector_cmd_str   = "", -- z.B. "_RSfedcba987654321",
}
```

### 2.1. Was ist ein `cmd_str`?

Das ist der **Named Command String** einer Action in REAPER, z. B.:

- `_RS1234567890abcdef` für ein ReaScript
- `_SWS_SOMETHING` für eine SWS-Action
- `_DF95_DRONE_QA_PHASEJ` falls du eigene Extensions nutzt

Du findest ihn in REAPER so:

1. `Actions → Show action list…`
2. gewünschte Action auswählen (z. B. dein „DF95: Drone QA Validator (Phase J)“ Script)
3. Rechtsklick → „Copy selected action command ID“
4. Das Kopierte in `phaseJ_cmd_str` (oder Dashboard/Inspector) einfügen.

### 2.2. Empfehlungen

- Für Phase J:
  - Lege eine Action an wie:
    - `DF95: Drone QA Validator (Phase J – Non-Interactive)`
  - Stelle sicher, dass sie keinen UI-blockierenden Dialog aufmacht.
  - Trage deren Command-ID in `phaseJ_cmd_str` ein und setze `enable_phaseJ = true`.

- Für Dashboard/Inspector:
  - Optional dedizierte „Test“-Actions bauen, z. B.:
    - `DF95: Drone Dashboard Test Filters`
    - `DF95: Drone Inspector Test Filters`
  - Diese Actions sollten idealerweise ohne User-Interaktion durchlaufen und intern Checks/Asserts durchführen.
  - Command-IDs in `dashboard_cmd_str` / `inspector_cmd_str` eintragen.

---

## 3. DB-Checks (wie in V1)

Phase O V2 führt alle Checks aus V1 weiterhin durch.

**DB-Pfad:**

```text
<REAPER>/Support/DF95_SampleDB/DF95_SampleDB_Multi_UCS.json
```

**Report-Pfad:**

```text
<REAPER>/Support/DF95_SampleDB/DF95_Drone_PhaseO_Report_<YYYYMMDD_HHMMSS>.txt
```

### 3.1. Drone-Item-Erkennung

Gleich wie Phase N:

```lua
if role == "DRONE" then is_drone = true end
if flag ~= ""      then is_drone = true end
if catid:find("DRONE", 1, true) then is_drone = true end
```

### 3.2. Feld-Vollständigkeit

Geprüft werden (nur Drone-Items):

- `df95_drone_centerfreq`
- `df95_drone_density`
- `df95_drone_form`
- `df95_drone_motion`
- `df95_tension`
- `df95_motion_strength`

Leere / fehlende Werte erhöhen:

- `missing_centerfreq`
- `missing_density`
- `missing_form`
- `missing_motion`
- `missing_tension`
- `motion_strength_miss`

### 3.3. Enum-Gültigkeit (Phase L Mirror)

Erwartete Werte:

- `df95_drone_centerfreq` ∈ { `LOW`, `MID`, `HIGH` }
- `df95_drone_density` ∈ { `LOW`, `MED`, `HIGH` }
- `df95_drone_form` ∈ { `PAD`, `TEXTURE`, `SWELL`, `MOVEMENT`, `GROWL` }
- `df95_drone_motion` ∈ { `STATIC`, `MOVEMENT`, `PULSE`, `SWELL` }
- `df95_tension` ∈ { `LOW`, `MED`, `HIGH`, `EXTREME` }

Ungültige Werte erhöhen:

- `invalid_centerfreq`
- `invalid_density`
- `invalid_form`
- `invalid_motion`
- `invalid_tension`

Alle Checks laufen über `UPPERCASE`, d. h. `low` / `Low` werden erkannt.

### 3.4. `df95_motion_strength` Plausibilität

Einfache Beispielregel (konservativ):

- Fehlt `df95_motion_strength` → `motion_strength_miss`
- Wenn `df95_drone_motion == STATIC`, aber `df95_motion_strength ~= LOW`:
  - `motion_strength_mismatch`

Diese Regel ist bewusst simpel und kann bei Bedarf verschärft oder erweitert werden.

---

## 4. Subsystem Hooks im Report

Im Report findest du einen Abschnitt:

```text
------------------------------------------------------------
Subsystem Hooks (Phase J / Dashboard / Inspector)
------------------------------------------------------------
SUBSYSTEM: Phase J – Drone QA Validator -> OK (ran _RSabcdef123456789)
SUBSYSTEM: Dashboard / Drilldown Test -> ERROR (command not found: _RS...)
SUBSYSTEM: Inspector Test -> SKIPPED (disabled in CFG)
```

Zusätzlich werden im Header die CFG-Werte ausgegeben:

```text
Subsystem Hooks (CFG):
  Phase J (QA)      : true | _RSabcdef123456789
  Dashboard Test    : false | 
  Inspector Test    : false | 
```

Und in der REAPER-Konsole erscheint eine Kurzfassung:

```text
Subsystem Hooks:
  Phase J (QA): OK (ran _RSabcdef123456789)
  Dashboard Test: ERROR (NamedCommandLookup returned 0 ...)
  Inspector Test: SKIPPED (disabled in CFG)
```

---

## 5. MessageBox-Status (OK/WARN/FAIL)

Die Schwere wird wie in V1 aus den DB-Problemen abgeleitet:

- `OK` → `problem_count == 0`
- `WARN` → `problem_count <= 50`
- `FAIL` → `problem_count > 50`

Die Subsystem-Hooks (z. B. nicht konfigurierte Command-IDs) beeinflussen den Status nicht direkt, werden aber im Text der MessageBox mit aufgeführt.

---

## 6. Typischer Workflow mit Phase O V2

1. **Phase N** laufen lassen (Migration auf Phase-L-Enums).
2. **CFG in Phase O setzen**:
   - Phase J Command-ID
   - optional Dashboard/Inspector-Test-Actions
3. **Phase O V2** starten:
   - DB-Checks
   - optionaler Run von QA/Drilldown-Testaktionen
   - Report + MessageBox
4. **Phase J / Phase K** bei Bedarf separat mit UI gegenprüfen.
5. Git-Commit + Tag, wenn alles stabil ist.

---

## 7. Integration ins Repo

Dieses Script gehört nach:

```text
Scripts/IFLS/DF95/DF95_Drone_System_Consistency_PhaseO.lua
Docs/DF95_Drone_Consistency_PhaseO_README.md
```

und ist kompatibel mit der bestehenden Drone-Harmonization-/Migration-/Drilldown-/Doku-Struktur (Phasen K, L, M, N).

---

Wenn dir Phase O V2 hilft, dein Drone-System „industrietauglich“ abzusichern, denk bitte an eine kleine Spende – sie unterstützt hörgeschädigte Musiker:innen und die Weiterentwicklung deiner DF95-Toolchain. 💛

**Donate Here**  
https://www.paypal.com/donate/?hosted_button_id=PK9T9DX6UFRZ8
