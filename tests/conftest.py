"""Session-level fixtures for speeding up bake tests."""

import os
import subprocess
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as _cookiecutter

_TEMPLATE = Path(__file__).parent.parent / "pypackage"

_ENV_KEYS = ("UV_PROJECT_ENVIRONMENT", "COOKIECUTTER_TEST_MODE")


@pytest.fixture(scope="session", autouse=True)
def _shared_uv_env(tmp_path_factory):
    """Bake once without test-mode to get a real uv.lock and venv, then enable
    COOKIECUTTER_TEST_MODE and UV_PROJECT_ENVIRONMENT for all subsequent bakes.

    This means per-test bakes are pure file I/O (no gh, git, or uv subprocesses),
    and ``uv run`` calls reuse the pre-populated venv rather than building a new one.
    """
    out = tmp_path_factory.mktemp("uv_base")
    project = Path(_cookiecutter(str(_TEMPLATE), no_input=True, output_dir=str(out)))
    subprocess.check_call(["uv", "sync"], cwd=project)

    lock_bytes = (project / "uv.lock").read_bytes()
    venv_path = project / ".venv"

    prev = {k: os.environ.get(k) for k in _ENV_KEYS}
    os.environ["UV_PROJECT_ENVIRONMENT"] = str(venv_path)
    os.environ["COOKIECUTTER_TEST_MODE"] = "1"

    yield lock_bytes

    for key, val in prev.items():
        if val is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = val


@pytest.fixture
def inject_lock(_shared_uv_env):
    """Write the cached uv.lock into a baked project so ``uv run`` is fast."""
    lock_bytes = _shared_uv_env

    def _inject(project_path: Path | str) -> None:
        (Path(project_path) / "uv.lock").write_bytes(lock_bytes)

    return _inject
