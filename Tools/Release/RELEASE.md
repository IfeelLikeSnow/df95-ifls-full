# DF95 Release-Template (Tag + index bump)

Dieses Template beschreibt einen **„minimalen Release-Prozess“**: keine Features kürzen, nur sauber versionieren
und ReaPack-Updates zuverlässig ausliefern.

## 0) Vorbedingungen (lokal)
- Git installiert
- Repo sauber (keine uncommitted Änderungen)

## 1) Version festlegen (SemVer)
Siehe `Tools/Release/SEMVER_DF95.md`.

Beispiel:
- Bugfix-only → `3.0.1`
- Neue Features ohne Break → `3.1.0`
- Breaking → `4.0.0`

## 2) Changelog aktualisieren
- `DF95_Changelog.txt` oben um neuen Abschnitt ergänzen (Datum + Highlights)
- optional: Links zu Issues/PRs

## 3) ReaPack index bump
Führt das Script aus:

```bash
python3 Tools/Release/bump_reapack_version.py 3.0.1
```

Das Script:
- setzt **alle** `<version name="...">` Einträge in `index.xml` auf die neue Version
- aktualisiert `time=` (UTC epoch)
- optional: kann später um „pro Pack unterschiedliche Version“ erweitert werden (aktuell bewusst einheitlich)

## 4) Commit + Tag + Push
```bash
git add index.xml DF95_Changelog.txt
git commit -m "Release v3.0.1"
git tag -a v3.0.1 -m "DF95 v3.0.1"
git push origin main --tags
```

## 5) ReaPack-Update testen
In REAPER:
- Extensions → ReaPack → **Manage repositories**
- euer Repo auswählen → **Refresh / Synchronize packages**
- prüfen: Updates erscheinen (u-Status) und installieren.

## 6) Rollback (falls nötig)
- Git tag entfernen oder neuen Patch release (empfohlen)
- ReaPack-seitig: User können Packages pinnen (optional – je nach Setup)

