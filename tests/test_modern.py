"""Tests for modern Python features in PyQuickRef."""

from collections.abc import Callable
from typing import Any


def test_dataclass_example(quickref: Any, capture_output: Callable) -> None:
    """Test dataclass example."""
    output = capture_output(quickref.dataclass_example)
    assert "Point(x=3.0, y=4.0)" in output
    assert "Distance to origin: 5.0" in output
    assert "Points equal: True" in output
    assert "Config" in output


def test_pattern_matching(quickref: Any, capture_output: Callable) -> None:
    """Test pattern matching example."""
    output = capture_output(quickref.pattern_matching)
    assert "HTTP 200: OK" in output
    assert "HTTP 404: Not Found" in output
    assert "Circle with radius 5" in output
    assert "Rectangle 3x4" in output


def test_generator_example(quickref: Any, capture_output: Callable) -> None:
    """Test generator example."""
    output = capture_output(quickref.generator_example)
    assert "Fibonacci(8): [0, 1, 1, 2, 3, 5, 8, 13]" in output
    assert "Generator expression: [0, 1, 4, 9, 16]" in output
    assert "Values > 4" in output


def test_enum_example(quickref: Any, capture_output: Callable) -> None:
    """Test enum example."""
    output = capture_output(quickref.enum_example)
    assert "Color.RED" in output
    assert "RED is warm" in output
    assert "BLUE is cool" in output
