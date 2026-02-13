"""Tests for class and OOP examples."""

from collections.abc import Callable

from pyquickref.examples.classes import (
    class_basics,
    dunder_methods,
    multiple_inheritance,
)


def test_class_basics(capture_output: Callable) -> None:
    """Test class definitions, inheritance, and class methods."""
    output = capture_output(class_basics)
    assert "Cat says meow" in output
    assert "Rex" in output
    assert "woof" in output
    assert "fetches the ball" in output
    assert "radius=5.0" in output
    assert "100°C = 212.0°F" in output


def test_dunder_methods(capture_output: Callable) -> None:
    """Test special (dunder) methods."""
    output = capture_output(dunder_methods)
    assert "Vector(1, 2)" in output
    assert "(1, 2)" in output
    assert "v1 + v2" in output
    assert "v1 == Vector(1, 2)? True" in output
    assert "v1 < v2? True" in output
    assert "len(v1) = 2" in output


def test_multiple_inheritance(capture_output: Callable) -> None:
    """Test multiple inheritance and MRO."""
    output = capture_output(multiple_inheritance)
    assert "Hello from B" in output
    assert "MRO:" in output
    assert "Init order:" in output
