"""Shared test fixtures and configuration."""

import logging
import os
import sys
import tempfile
from collections.abc import Generator
from pathlib import Path
from typing import Any, Callable, TypeVar

# Import pytest first, then update the path
import pytest
from pytest import CaptureFixture

# Update the import path to use the new package structure
sys.path.insert(0, str(Path(__file__).parent.parent))
# Now import from the project
from pyquickref.core import PyQuickRef  # noqa: E402

F = TypeVar("F", bound=Callable[..., Any])


@pytest.fixture
def temp_dir() -> Generator[str, None, None]:
    """Provide a temporary directory for test outputs."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Store the original working directory
        original_dir = os.getcwd()
        # Change to the temporary directory for tests
        os.chdir(tmp_dir)
        yield tmp_dir
        # Change back to the original directory
        os.chdir(original_dir)


@pytest.fixture
def quickref(temp_dir: str) -> PyQuickRef:
    """Create a PyQuickRef instance for testing."""
    # Set up a logger that doesn't output anything during tests
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.CRITICAL)
    # Initialize PyQuickRef instance with output directory
    output_dir = os.path.join(temp_dir, "output")
    return PyQuickRef(logger, output_dir=output_dir)


@pytest.fixture
def capture_output(
    capsys: CaptureFixture[str],
) -> Callable[..., str]:
    """Capture stdout from a function call."""

    def _capture(func: Callable[..., Any], *args: Any, **kwargs: Any) -> str:
        func(*args, **kwargs)
        return str(capsys.readouterr().out)  # Explicitly ensure the return type is str

    return _capture


def some_function() -> str:
    """Return a sample string for testing purposes."""
    return "some_string"  # Replace with the actual implementation if needed
