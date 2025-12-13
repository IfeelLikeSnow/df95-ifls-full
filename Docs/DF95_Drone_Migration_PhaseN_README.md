\
# DF95 Drone Migration – Phase N

**Script:** `Scripts/IFLS/DF95/DF95_SampleDB_Drone_Migrate_PhaseN.lua`  
**Ziel:** Einmalige Normalisierung aller Drone-bezogenen Felder in deiner DF95 SampleDB auf die harmonisierten Phase-L-Enums. 🧠🌀🧹

---

## 1. Zweck von Phase N

Phase N sorgt dafür, dass alle Drone-Felder in deiner SampleDB konsistent und zukunftssicher auf den **Phase-L-Enums** basieren.

**Betroffene Felder:**

- `df95_drone_centerfreq` → `LOW`, `MID`, `HIGH`
- `df95_drone_density` → `LOW`, `MED`, `HIGH`
- `df95_drone_form` → `PAD`, `TEXTURE`, `SWELL`, `MOVEMENT`, `GROWL`
- `df95_drone_motion` → `STATIC`, `MOVEMENT`, `PULSE`, `SWELL`
- `df95_motion_strength` → synchron zu `df95_drone_motion`
- `df95_tension` → `LOW`, `MED`, `HIGH`, `EXTREME`

Die eigentliche Normalisierung übernimmt **Phase L**:

```lua
local DF95_DroneEnums = dofile(reaper.GetResourcePath()
  .. "/Scripts/IFLS/DF95/DF95_Drone_Enums_PhaseL.lua")

DroneEnums.normalize_item_drone_fields(it)
```

Phase N ruft diese Funktion für jedes Drone-Item der SampleDB auf und zählt alle Änderungen.

---

## 2. Ziel-DB und Backup

**DB-Pfad:**

```text
<REAPER>/Support/DF95_SampleDB/DF95_SampleDB_Multi_UCS.json
```

Vor jeder Änderung erzeugt Phase N automatisch ein Backup:

```text
DF95_SampleDB_Multi_UCS_backup_<YYYYMMDD_HHMMSS>.json
```

- Das Backup liegt im **gleichen Ordner** wie die Haupt-DB.
- Im Fehlerfall kannst du die Backup-Datei einfach wieder in
  `DF95_SampleDB_Multi_UCS.json` zurückkopieren.

Zusätzlich legt das Script eine Marker-Datei an:

```text
DF95_Drone_PhaseN_COMPLETE.txt
```

Darin:

- Timestamp der Migration
- Name der Backup-Datei
- Statistik (Total Items, Drone-Items, Änderungen pro Feld)

---

## 3. Welche Items gelten als „Drone“?

Phase N erkennt Drone-Items so, wie es in deinem System
(Inspector, Dashboard, AutoIngest) etabliert ist.

Im Script (vereinfacht):

```lua
local role  = upper(it.role)
local flag  = upper(it.df95_drone_flag)
local catid = upper(it.df95_catid or "")
local is_drone = false

if role == "DRONE" then is_drone = true end
if flag ~= ""      then is_drone = true end
if catid:find("DRONE", 1, true) then is_drone = true end
```

Ein Item gilt also als Drone, wenn **mindestens eine** der Bedingungen erfüllt ist:

1. `role == "Drone"` (case-insensitive)  
2. `df95_drone_flag` ist nicht leer  
3. `df95_catid` enthält den String `"DRONE"`

Das ist konsistent mit:

- AutoIngest
- Dashboard
- Inspector
- bestehenden Filter- und Drilldown-Logiken

---

## 4. Was genau wird gezählt & geändert?

Für jedes Drone-Item speichert Phase N intern vor/nach:

- `before_cf` / `after_cf` → `df95_drone_centerfreq`
- `before_dens` / `after_dens` → `df95_drone_density`
- `before_form` / `after_form` → `df95_drone_form`
- `before_mot` / `after_mot` → `df95_drone_motion`
- `before_ten` / `after_ten` → `df95_tension`

Und zählt:

- **Gesamtanzahl** der Drone-Items mit Änderungen:
  - `changed_any`
- Feld-spezifische Änderungen:
  - `changed_centerfreq`
  - `changed_density`
  - `changed_form`
  - `changed_motion`
  - `changed_tension`

Am Ende erscheint in der REAPER-Konsole ein Report im Stil:

```text
Total Items: 12345
Drone-Items: 678
Drone-Items mit Änderungen: 210

Feldweise Änderungen (bei Drone-Items):
  centerfreq: 50
  density   : 120
  form      : 80
  motion    : 200
  tension   : 60

Backup: ...DF95_SampleDB_Multi_UCS_backup_20251129_213012.json
Migration erfolgreich abgeschlossen.

Phase N Migration done – Bier-Zeit! 🍺
```

---

## 5. Wie du Phase N verwendest (Kurzfassung)

1. **Repo-Struktur mergen**

   Das Phase-N-Paket ist so gebaut, dass du es direkt in dein bestehendes
   DF95-Repo integrieren kannst:

   - Script nach  
     `Scripts/IFLS/DF95/DF95_SampleDB_Drone_Migrate_PhaseN.lua`
   - Diese README nach  
     `Docs/DF95_Drone_Migration_PhaseN_README.md`

   Phase-L-Enums (`DF95_Drone_Enums_PhaseL.lua`) sollten bereits vorhanden sein.

2. **Script in REAPER laden**

   - `Actions → Show action list…`
   - Reiter **ReaScript**
   - `Load…`
   - `DF95_SampleDB_Drone_Migrate_PhaseN.lua` auswählen
   - Optional: Action umbenennen in  
     `DF95: Drone SampleDB – Phase N Migration (ONE-TIME)`

3. **Script ausführen**

   - Beim Start erscheint ein Confirm-Dialog
   - Das Script legt ein Backup an
   - Die Migration wird durchgeführt
   - Am Ende:
     - Konsolen-Report
     - Abschluss-Dialog („Phase-N-Bier“)

4. **Nach der Migration**

   - `Drone QA Validator (Phase J)` laufen lassen
   - `Dashboard & Inspector` Drilldown testen
   - Git-Commit + Tag setzen
   - Offiziell: **Phase-N-Bier öffnen** 🍺

---

## 6. Integration in deinen Workflow

Phase N ist idealer Bestandteil eines DF95-Maintenance-Workflows:

1. **Enums aktualisieren (Phase L)**
2. **Phase N – DB Migration**
3. **Phase J – Drone QA Validator**
4. **Phase K – Dashboard / Inspector Smoke-Test**
5. **Versionierung (Git-Tag, Release)**
6. **„Phase N Bier“ – Ritualabschluss**

---

## 7. Nächste sinnvolle Schritte

Mit erfolgreicher Phase-N-Migration hast du:

- harmonisierte Drone-Enums (Phase L)
- eine konsistent migrierte SampleDB (Phase N)
- QA-Tools (Phase J)
- Drilldown/Filter-UX (Phase K)
- Dokumentation (Phase M)

Damit ist dein Drone-System **technisch vollständig**.

Sinnvolle nächste Ausbaustufen:

1. **Mini-Rollback-Tool (Safety Net)**  
   - Backup-Dateien auflisten  
   - „SampleDB auf Zustand X zurücksetzen“

2. **Phase O – Full Drone System Consistency Test**  
   - DB-Checks nach Phase N  
   - QA Validator anstoßen  
   - Dashboard/Inspector Filter per Dry-Run prüfen  
   - Report mit OK/FAIL pro Subsystem

3. **Creative Producer Features (Phase P)**  
   - Vorschläge: „Drones, die dir noch fehlen“  
   - Balanced-Score für die Drone-Library  
   - Auto-Vorschläge für Recording-Sessions  
     (z. B. „mehr LOW_STATIC_HOME Drones aufnehmen“)

---

Wenn dir Phase N hilft, deine Drone-Library sauber und zukunftssicher zu halten, denk bitte an eine kleine Spende – sie unterstützt hörgeschädigte Musiker:innen und die Weiterentwicklung deiner DF95-Toolchain. 💛

**Donate Here**  
https://www.paypal.com/donate/?hosted_button_id=PK9T9DX6UFRZ8
