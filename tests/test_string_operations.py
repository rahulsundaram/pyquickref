"""Tests for string operations in PyQuickRef."""

from typing import Any, Callable


def test_string_operations(quickref: Any, capture_output: Callable) -> None:
    """Test string operations."""
    output = capture_output(quickref.string_operations)
    # The test needs to match the actual string used in main.py
    assert "Python is awesome" in output
    assert "PYTHON IS AWESOME" in output
    assert "Hello, World!" in output
