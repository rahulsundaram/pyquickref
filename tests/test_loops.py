"""Tests for loop operations."""

from collections.abc import Callable

from pyquickref.examples.loops import loop_range


def test_loop_range(capture_output: Callable) -> None:
    """Test loop constructs: range, enumerate, zip, while, continue."""
    output = capture_output(loop_range)
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
