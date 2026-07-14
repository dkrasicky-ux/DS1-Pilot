from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
if str(ROOT / "DS1-Pilot") not in sys.path:
    sys.path.insert(0, str(ROOT / "DS1-Pilot"))

from ds1_pilot_dashboard import main


if __name__ == "__main__":
    main()
