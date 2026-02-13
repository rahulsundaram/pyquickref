"""Tests for modules and packaging examples."""

from collections.abc import Callable

from pyquickref.examples.modules_packaging import import_system, packaging_example


def test_import_system(capture_output: Callable) -> None:
    """Test import system demonstration."""
    output = capture_output(import_system)
    assert "Absolute imports" in output
    assert "Relative imports" in output
    assert "__init__.py" in output
    assert "__all__" in output
    assert "sys.path has" in output
    assert "__name__" in output


def test_packaging_example(capture_output: Callable) -> None:
    """Test packaging concepts demonstration."""
    output = capture_output(packaging_example)
    assert "python -m" in output
    assert "pyproject.toml" in output
    assert "[project]" in output
    assert "src/ layout" in output
    assert "uv build" in output
