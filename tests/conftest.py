"""Shared test fixtures and configuration."""

import logging
import os
import tempfile
from collections.abc import Callable, Generator
from typing import Any

import pytest
from pytest import CaptureFixture

from pyquickref.core import PyQuickRef


@pytest.fixture
def temp_dir() -> Generator[str, None, None]:
    """Provide a temporary directory for test outputs."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        original_dir = os.getcwd()
        os.chdir(tmp_dir)
        yield tmp_dir
        os.chdir(original_dir)


@pytest.fixture
def quickref(temp_dir: str) -> PyQuickRef:
    """Create a PyQuickRef instance for testing."""
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.CRITICAL)
    output_dir = os.path.join(temp_dir, "output")
    return PyQuickRef(logger, output_dir=output_dir)


@pytest.fixture
def capture_output(
    capsys: CaptureFixture[str],
) -> Callable[..., str]:
    """Capture stdout from a function call."""

    def _capture(func: Callable[..., Any], *args: Any, **kwargs: Any) -> str:
        func(*args, **kwargs)
        return str(capsys.readouterr().out)

    return _capture
