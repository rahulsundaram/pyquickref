"""Tests for modern Python features."""

from collections.abc import Callable

from pyquickref.examples.modern import (
    dataclass_example,
    enum_example,
    generator_example,
    pattern_matching,
    type_hints,
    walrus_operator,
)


def test_dataclass_example(capture_output: Callable) -> None:
    """Test dataclass example."""
    output = capture_output(dataclass_example)
    assert "Point(x=3.0, y=4.0)" in output
    assert "Distance to origin: 5.0" in output
    assert "Points equal: True" in output
    assert "Config" in output


def test_pattern_matching(capture_output: Callable) -> None:
    """Test pattern matching example."""
    output = capture_output(pattern_matching)
    assert "HTTP 200: OK" in output
    assert "HTTP 404: Not Found" in output
    assert "Circle with radius 5" in output
    assert "Rectangle 3x4" in output


def test_generator_example(capture_output: Callable) -> None:
    """Test generator example."""
    output = capture_output(generator_example)
    assert "Fibonacci(8): [0, 1, 1, 2, 3, 5, 8, 13]" in output
    assert "Generator expression: [0, 1, 4, 9, 16]" in output
    assert "Values > 4" in output


def test_enum_example(capture_output: Callable) -> None:
    """Test enum example."""
    output = capture_output(enum_example)
    assert "Color.RED" in output
    assert "RED is warm" in output
    assert "BLUE is cool" in output


def test_walrus_operator(capture_output: Callable) -> None:
    """Test walrus operator examples."""
    output = capture_output(walrus_operator)
    assert "Values > 4:" in output
    assert "Squares > 20:" in output
    assert "characters" in output


def test_type_hints(capture_output: Callable) -> None:
    """Test type hints example."""
    output = capture_output(type_hints)
    assert "annotated as str" in output
    assert "annotated as list[int]" in output
    assert "find_user(1) = 'Alice'" in output
    assert "find_user(9) = None" in output
    assert "dict[str, float]" in output
