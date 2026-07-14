from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def test_root_entrypoint_exists():
    app_path = Path(__file__).parent / "app.py"
    assert app_path.exists(), "Expected a root app entrypoint for Streamlit deployment"


def test_root_entrypoint_exports_main():
    app_path = Path(__file__).parent / "app.py"
    spec = spec_from_file_location("app", app_path)
    module = module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    assert callable(module.main)
