"""Environment smoke test for the PM2.5 forecasting project.

This is the deliverable required by Issue #01:

    "Viết script kiểm thử môi trường xác nhận nạp thành công toàn bộ thư viện
     trên Windows/Linux" — acceptance: "chạy với mã thoát 0".

It deliberately tests *environment reproducibility* rather than modelling
behaviour, because the modelling pipeline does not exist yet. The checks are:

1. The running interpreter is inside the supported Python window.
2. The supported window declared in ``requirements.txt`` matches the one
   this module hard-codes, so the two cannot silently drift apart.
3. Every distribution named in ``requirements.txt`` is actually installed.
4. Every installed distribution satisfies the constraint that
   ``requirements.txt`` resolves to *on this interpreter* (i.e. the
   ``python_version`` markers are applied, not ignored).
5. The public API surface the project depends on really exists in the
   installed versions.

Run with::

    python -m unittest discover -s tests -v
"""

from __future__ import annotations

import importlib
import importlib.metadata
import re
import sys
import unittest
from pathlib import Path

from packaging.requirements import Requirement

REPO_ROOT = Path(__file__).resolve().parent.parent
REQUIREMENTS_FILE = REPO_ROOT / "requirements.txt"

#: Inclusive, exclusive upper bound of the Python versions this project
#: supports. Keep in sync with the SUPPORTED PYTHON banner in
#: requirements.txt -- test_declared_window_matches_module_constant()
#: fails loudly if they ever disagree.
SUPPORTED_PYTHON_MIN = (3, 10)
SUPPORTED_PYTHON_MAX = (3, 14)

#: Distributions whose PyPI name differs from their importable module name.
IMPORT_NAME_OVERRIDES = {
    "pyyaml": "yaml",
    "scikit-learn": "sklearn",
    # `jupyter` is a metapackage: it ships the `jupyter` executable and
    # declares no importable module, so only its metadata can be checked.
    "jupyter": None,
}


def _parse_requirements() -> list[Requirement]:
    """Parse requirements.txt, ignoring comments and blank lines."""
    requirements: list[Requirement] = []
    for raw_line in REQUIREMENTS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        requirements.append(Requirement(line))
    return requirements


def _declared_window() -> tuple[tuple[int, int], tuple[int, int]] | None:
    """Read the SUPPORTED PYTHON banner out of requirements.txt."""
    text = REQUIREMENTS_FILE.read_text(encoding="utf-8")
    match = re.search(
        r"^#\s*SUPPORTED PYTHON:\s*(\d+\.\d+)\s*[\u2013\u2014-]\s*(\d+\.\d+)\s*$",
        text,
        re.MULTILINE,
    )
    if match is None:
        return None
    low, high = match.group(1), match.group(2)
    return (
        tuple(int(p) for p in low.split(".")),
        tuple(int(p) for p in high.split(".")),
    )


def _active_requirements() -> list[Requirement]:
    """Requirements whose environment marker matches the running interpreter."""
    return [
        req
        for req in _parse_requirements()
        if req.marker is None or req.marker.evaluate()
    ]


class TestSupportedPython(unittest.TestCase):
    """Checks 1 and 2: the interpreter and the declared window."""

    def test_running_interpreter_is_supported(self):
        version = sys.version_info[:2]
        self.assertGreaterEqual(
            version,
            SUPPORTED_PYTHON_MIN,
            f"Python {'.'.join(map(str, version))} is below the supported floor "
            f"{'.'.join(map(str, SUPPORTED_PYTHON_MIN))}.",
        )
        self.assertLessEqual(
            version,
            SUPPORTED_PYTHON_MAX,
            f"Python {'.'.join(map(str, version))} is above the supported ceiling "
            f"{'.'.join(map(str, SUPPORTED_PYTHON_MAX))}. "
            "Widen SUPPORTED_PYTHON only after confirming that every pinned "
            "upper cap in requirements.txt still resolves to a binary wheel.",
        )

    def test_declared_window_matches_module_constant(self):
        declared = _declared_window()
        self.assertIsNotNone(
            declared,
            "requirements.txt must carry a '# SUPPORTED PYTHON: <min> - <max>' banner.",
        )
        self.assertEqual(
            declared,
            (SUPPORTED_PYTHON_MIN, SUPPORTED_PYTHON_MAX),
            "The supported Python window in requirements.txt has drifted from "
            "SUPPORTED_PYTHON_MIN/SUPPORTED_PYTHON_MAX in tests/test_environment.py.",
        )


class TestDeclaredDependencies(unittest.TestCase):
    """Checks 3 and 4: presence and constraint satisfaction."""

    def test_requirements_file_is_parseable(self):
        requirements = _parse_requirements()
        self.assertGreater(
            len(requirements), 0, "requirements.txt declared no requirements."
        )
        self.assertTrue(
            _active_requirements(),
            "No requirement's environment marker matched this interpreter, so "
            "`pip install -r requirements.txt` would install nothing here.",
        )

    def test_every_declared_distribution_is_installed(self):
        missing: list[str] = []
        for req in _active_requirements():
            try:
                importlib.metadata.version(req.name)
            except importlib.metadata.PackageNotFoundError:
                missing.append(req.name)
        self.assertEqual(
            missing,
            [],
            f"Missing distribution(s): {missing}. "
            "Run `pip install -r requirements.txt`.",
        )

    def test_installed_versions_satisfy_constraints(self):
        violations: list[str] = []
        for req in _active_requirements():
            try:
                installed = importlib.metadata.version(req.name)
            except importlib.metadata.PackageNotFoundError:
                continue  # already reported by the test above
            if not req.specifier.contains(installed, prereleases=True):
                violations.append(f"{req.name} {installed} does not satisfy '{req.specifier}'")
        self.assertEqual(violations, [], "; ".join(violations))

    def test_only_one_branch_per_marked_distribution(self):
        """A distribution must not resolve to two different pins at once.

        Guards against a copy/paste error that leaves both marker branches
        active on the same interpreter, which pip would reject or silently
        resolve to the wrong line.
        """
        seen: dict[str, set[str]] = {}
        for req in _parse_requirements():
            if req.marker is None:
                continue
            seen.setdefault(req.name, set()).add(str(req.specifier))
        self.assertTrue(seen, "Expected at least one environment-marked requirement.")
        for name, specifiers in seen.items():
            self.assertGreater(
                len(specifiers),
                1,
                f"{name} has an environment marker but only one branch, so the "
                "marker is dead weight -- either drop it or add the other branch.",
            )


class TestPublicApiSurface(unittest.TestCase):
    """Check 5: the symbols the planned pipeline will rely on exist."""

    def test_data_and_numerics_import(self):
        for module in ("pandas", "numpy", "scipy", "pyarrow", "yaml"):
            with self.subTest(module=module):
                importlib.import_module(module)

    def test_classical_ml_api_exists(self):
        import lightgbm
        import sklearn
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.linear_model import Ridge
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
        from sklearn.preprocessing import StandardScaler

        self.assertTrue(hasattr(sklearn, "__version__"))
        self.assertTrue(hasattr(lightgbm, "LGBMRegressor"))
        for symbol in (
            RandomForestRegressor,
            Ridge,
            StandardScaler,
            mean_absolute_error,
            mean_squared_error,
            r2_score,
        ):
            self.assertTrue(callable(symbol))

    def test_deep_learning_api_exists(self):
        import torch
        from torch import nn
        from torch.utils.data import DataLoader

        self.assertTrue(hasattr(torch, "__version__"))
        self.assertTrue(hasattr(nn, "LSTM"))
        self.assertTrue(hasattr(DataLoader, "__init__"))

    def test_explainability_api_exists(self):
        import shap

        self.assertTrue(hasattr(shap, "TreeExplainer"))

    def test_serving_and_notebook_api_exists(self):
        import fastapi
        import pydantic
        import streamlit
        import uvicorn

        for module in (fastapi, pydantic, streamlit, uvicorn):
            self.assertTrue(hasattr(module, "__version__"))
        self.assertTrue(hasattr(fastapi, "FastAPI"))

    def test_mapped_and_metapackage_distributions_are_resolvable(self):
        for distribution, module in IMPORT_NAME_OVERRIDES.items():
            with self.subTest(distribution=distribution):
                # Metadata must resolve for every declared distribution,
                # including metapackages that expose no importable module.
                self.assertTrue(importlib.metadata.version(distribution))
                if module is not None:
                    importlib.import_module(module)


if __name__ == "__main__":
    unittest.main(verbosity=2)
