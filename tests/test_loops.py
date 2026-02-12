"""Tests for loop operations in PyQuickRef."""

from collections.abc import Callable
from typing import Any


def test_loop_range(quickref: Any, capture_output: Callable) -> None:
    """Test loop constructs: range, enumerate, zip, while, continue."""
    output = capture_output(quickref.loop_range)
    assert "Range(5):" in output
    assert "Enumerate:" in output
    assert "0: apple" in output
    assert "Zip:" in output
    assert "Alice is 25" in output
    assert "While loop (break at 3):" in output
    assert "count=2" in output
    assert "count=3" not in output
    assert "Continue (skip even):" in output
    assert "  1" in output
    assert "  3" in output
    assert "  5" in output
