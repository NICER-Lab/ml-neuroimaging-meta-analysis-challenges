from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[2]

# Path to the neuroquery data directory (ie clone of https://github.com/neuroquery/neuroquery_data)
NEUROQUERY_DATA_DIR = PROJECT_DIR / 'data' / 'neuroquery_data'
NEUROQUERY_MODEL_DIR = NEUROQUERY_DATA_DIR / "neuroquery_model"


