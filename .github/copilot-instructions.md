# Copilot instructions for the `earthquakes` exercise

This repository is a small teaching exercise (single-module Python) that downloads and analyses USGS earthquake GeoJSON. The goal is to find the strongest earthquake in the UK within the supplied time-range.

Quick context for an AI coding agent

- Big picture: single Python script (`earthquakes.py`) fetches GeoJSON from USGS (see `get_data`) and analyses it. A static sample of the downloaded response is present in `earthquakes.json` (120 features). The `README.md` explains the exercise and how students should run the script.

- Key files:
  - `earthquakes.py` — main program to inspect and complete. Contains functions: `get_data()`, `count_earthquakes(data)`, `get_magnitude(earthquake)`, `get_location(earthquake)`, and `get_maximum(data)` (used in the top-level script).
  - `earthquakes.json` — a full GeoJSON sample response. Use it to write offline tests or to inspect data structure.
  - `README.md` — exercise instructions and run hints.

Project-specific patterns and important notes

- Single-file exercise: prefer minimal, clear edits inside `earthquakes.py`. There is no package structure, virtualenv config, or test harness in the repo.

- Network I/O: `get_data()` calls `requests.get(...)` with specific query params (bounded lat/long, dates, min magnitude). Tests or changes should avoid hitting the real USGS API during grading; prefer reading `earthquakes.json` or mocking `requests` when possible.

- Data shape expectations: the GeoJSON top-level keys include `metadata` (with `count`) and `features` (list of Feature objects). Each feature uses `properties.mag` for magnitude and `geometry.coordinates` as [lon, lat, depth]. Example use in the repo:
  - count: `data["metadata"]["count"]`
  - mag: `earthquake["properties"]["mag"]`
  - coords: `earthquake["geometry"]["coordinates"]` (unpack as lon, lat, depth)

- Defensive coding expectations: student-facing exercises expect readable, explanatory changes. Keep functions small and clearly named. Use the provided `README.md` phrasing when producing output (e.g., printing counts and final result).

Developer workflows (how to run and debug)

- Run script locally with the system Python (the README uses `python earthquakes.py`). On macOS with zsh, run from the repo folder:

```bash
python earthquakes.py
```

- To run offline or avoid network calls, temporarily modify `get_data()` to load from `earthquakes.json` or patch `requests.get` in tests/mocks.

- There is no test framework included. If you add tests, prefer `pytest` and a small fixture that loads `earthquakes.json`.

What to avoid / constraints

- Don't add heavy dependencies or change the pedagogical nature of the exercise (keep changes minimal and easy to explain).
- Avoid committing large autoformatted changes across unrelated files.

Examples of safe edits

- Improve `get_data()` to detect an environment variable (e.g., `USE_LOCAL_DATA=true`) and load `earthquakes.json` when set.
- Add a small helper function `load_local_data(path)` used by `get_data()` to fallback to the local file for offline runs.
- Add a short `if __name__ == '__main__':` guard to make functions import-safe (the current file runs on import).

If you need clarification

- Ask what output format the instructor expects (text only, specific wording). If asked to add tests, confirm whether adding `pytest` to the repo is acceptable.

References (files to open first)

- `earthquakes.py` — primary source of truth
- `earthquakes.json` — example payload to inspect
- `README.md` — exercise description and run guidance

End of instructions.
