"""Tests for advanced OOP examples."""

from collections.abc import Callable

from pyquickref.examples.advanced_oop import (
    descriptors_example,
    metaclass_example,
    protocols_abcs,
)


def test_descriptors_example(capture_output: Callable) -> None:
    """Test descriptor protocol demonstration."""
    output = capture_output(descriptors_example)
    assert "price=" in output
    assert "qty=" in output
    assert "Caught:" in output
    assert "non-negative" in output
    assert "property has __get__: True" in output


def test_metaclass_example(capture_output: Callable) -> None:
    """Test metaclass and __init_subclass__ demonstration."""
    output = capture_output(metaclass_example)
    assert "type(MyClass) = type" in output
    assert "obj.x = 10" in output
    assert "AuthPlugin" in output
    assert "CachePlugin" in output
    assert "__init_subclass__ tracked" in output


def test_protocols_abcs(capture_output: Callable) -> None:
    """Test protocols and ABCs demonstration."""
    output = capture_output(protocols_abcs)
    assert "isinstance(Circle(), Drawable) = True" in output
    assert "Drawing circle" in output
    assert "serialize" in output
    assert "isinstance(JsonRecord(), Serializable) = True" in output
    assert "Caught:" in output
