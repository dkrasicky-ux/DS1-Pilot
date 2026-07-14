# DS1 Pilot

A small Streamlit dashboard for exploring DS1 kitchen workflow concepts.

## Project layout

- `ds1_pilot_dashboard.py` — Streamlit app entrypoint
- `ds1_menu.py` — menu data used by the dashboard
- `ds1_core.py` — core station and inventory logic
- `tests/` — project tests
- `data/menu.json` — JSON-backed menu reference

## Run locally

From the repository root:

```bash
streamlit run app.py
```

## Testing

```bash
pytest -q
```
