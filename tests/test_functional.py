"""Tests for functional programming features in PyQuickRef."""

from collections.abc import Callable
from typing import Any


def test_lambda_functions(quickref: Any, capture_output: Callable) -> None:
    """Test lambda functions."""
    output = capture_output(quickref.lambda_functions)
    assert "Square of 5: 25" in output
    assert "Even numbers: [2, 4]" in output


def test_decorator_example(quickref: Any, capture_output: Callable) -> None:
    """Test decorator functionality."""
    output = capture_output(quickref.decorator_example)
    assert "Function slow_function took" in output
    assert "Function slept for 0.5 seconds" in output
    assert "Hello, Python!" in output


def test_itertools_examples(quickref: Any, capture_output: Callable) -> None:
    """Test itertools functionality."""
    output = capture_output(quickref.itertools_examples)
    assert "('A', 'B')" in output
    assert "Cycling through colors" in output
