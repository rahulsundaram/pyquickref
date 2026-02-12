"""Tests for control flow examples."""

from collections.abc import Callable

from pyquickref.examples.control_flow import for_while_loops, if_elif_else


def test_if_elif_else(capture_output: Callable) -> None:
    """Test if/elif/else, ternary, and truthiness."""
    output = capture_output(if_elif_else)
    assert "grade=B" in output
    assert "status=adult" in output
    assert "Truthiness:" in output
    assert "0      → False" in output
    assert "1      → True" in output


def test_for_while_loops(capture_output: Callable) -> None:
    """Test basic for and while loops."""
    output = capture_output(for_while_loops)
    assert "red" in output
    assert "green" in output
    assert "blue" in output
    assert "range(5):" in output
    assert "Powers of 2:" in output
    assert "Break at 5:" in output
    assert "Odd only:" in output
