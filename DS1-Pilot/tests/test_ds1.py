from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ds1_menu import get_menu
from ds1_math import risk_level
from ds1_station import calculate_station_load
from ds1_utils import format_time


def test_menu_contains_expected_items():
    menu = get_menu()
    assert menu
    assert any(item["name"] == "Brisket Sandwich" for item in menu)


def test_risk_level_thresholds():
    assert risk_level(0) == "Low"
    assert risk_level(2) == "Medium"
    assert risk_level(4) == "High"


def test_station_load_percentages():
    result = calculate_station_load({"Cutting": 5, "Assembly": 3, "Sides": 2})
    assert result["Cutting"] == 50.0
    assert result["Assembly"] == 30.0
    assert result["Sides"] == 20.0


def test_format_time_labels():
    assert format_time(8) == "8 min"
    assert format_time(0) == "Under 1 min"
