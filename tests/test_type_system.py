"""Tests for type system examples."""

from collections.abc import Callable

from pyquickref.examples.type_system import advanced_typing, generics_example


def test_generics_example(capture_output: Callable) -> None:
    """Test generic types with TypeVar and Generic."""
    output = capture_output(generics_example)
    assert "first([1, 2, 3])     = 1" in output
    assert "first(['a', 'b'])    = a" in output
    assert "Stack after pushes" in output
    assert "pop() =" in output
    assert "clamp(15, 0, 10)       = 10" in output


def test_advanced_typing(capture_output: Callable) -> None:
    """Test overload, TypeAlias, and ParamSpec."""
    output = capture_output(advanced_typing)
    assert "users:" in output
    assert "process('hello world')" in output
    assert "process(['hello', 'world'])" in output
    assert "Calling add" in output
    assert "Result: 7" in output
