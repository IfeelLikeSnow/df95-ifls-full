# Release Checklist (DF95)

## Pre-flight
- [ ] Smoke Test läuft „grün“ (keine missing core files)
- [ ] Install Doctor zeigt keine falschen Requires (SWS/Python sind ok, falls bei euch Standard)
- [ ] Master-Menü öffnet ohne Errors
- [ ] Folder-Scan Menü baut deterministisch (Sortierung ok)
- [ ] Wrapper-Imports (CSV/JSON) erzeugen `actions[]` (für A5/A6 Requires)

## Change log
- [ ] DF95_Changelog.txt aktualisiert
- [ ] Breaking changes explizit markiert (wenn MAJOR)

## Version bump
- [ ] `python3 Tools/Release/bump_reapack_version.py X.Y.Z`
- [ ] index.xml geprüft (5 Packs haben die neue Version + neue time)

## Publish
- [ ] Commit
- [ ] Annotated tag `vX.Y.Z`
- [ ] Push tags
- [ ] In REAPER ReaPack refresh: Update erscheint

