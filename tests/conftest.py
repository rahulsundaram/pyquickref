"""Shared test fixtures and configuration."""

import os
import tempfile
from collections.abc import Callable, Generator
from typing import Any

import pytest
from pytest import CaptureFixture

import pyquickref.examples  # noqa: F401  — trigger registration
from pyquickref.testdata import SampleData


@pytest.fixture
def temp_dir() -> Generator[str, None, None]:
    """Provide a temporary directory for test outputs."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        original_dir = os.getcwd()
        os.chdir(tmp_dir)
        yield tmp_dir
        os.chdir(original_dir)


@pytest.fixture
def sample_data() -> SampleData:
    """Provide a fresh SampleData instance (mutations are isolated per test)."""
    return SampleData()


@pytest.fixture
def output_dir(temp_dir: str) -> str:
    """Provide a temporary output directory for file-writing examples."""
    path = os.path.join(temp_dir, "output")
    os.makedirs(path)
    return path


@pytest.fixture
def capture_output(
    capsys: CaptureFixture[str],
) -> Callable[..., str]:
    """Capture stdout from a function call."""

    def _capture(func: Callable[..., Any], *args: Any, **kwargs: Any) -> str:
        func(*args, **kwargs)
        return str(capsys.readouterr().out)

    return _capture
