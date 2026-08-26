import json
from pathlib import Path

from app.main import app

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
OPENAPI_FILE = PROJECT_ROOT / "openapi.json"


def main() -> None:
    with open(OPENAPI_FILE, "w") as f:
        json.dump(app.openapi(), f, indent=2)
        f.write("\n")
