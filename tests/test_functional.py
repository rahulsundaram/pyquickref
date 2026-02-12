"""Tests for functional programming features."""

from collections.abc import Callable

from pyquickref.examples.functional import (
    builtin_functions,
    decorator_example,
    function_basics,
    lambda_functions,
    recursion_example,
    scope_closures,
)


def test_function_basics(capture_output: Callable) -> None:
    """Test function definitions, args, kwargs, return values."""
    output = capture_output(function_basics)
    assert "Hello, World!" in output
    assert "power(3)    = 9" in output
    assert "power(3, 3) = 27" in output
    assert "total(1, 2, 3) = 6" in output
    assert "page=1" in output
    assert "min=1, max=9" in output


def test_builtin_functions(capture_output: Callable) -> None:
    """Test any, all, sorted with key, min/max."""
    output = capture_output(builtin_functions)
    assert "All even? True" in output
    assert "Any > 5?  True" in output
    assert "By length:" in output
    assert "Youngest: Bob" in output
    assert "Oldest:   Charlie" in output


def test_scope_closures(capture_output: Callable) -> None:
    """Test scope rules and closures."""
    output = capture_output(scope_closures)
    assert "LEGB:" in output
    assert "local" in output
    assert "enclosing" in output
    assert "global" in output
    assert "Closure: 1, 2, 3" in output
    assert "double(5) = 10" in output
    assert "triple(5) = 15" in output


def test_recursion_example(capture_output: Callable) -> None:
    """Test recursive functions."""
    output = capture_output(recursion_example)
    assert "factorial(5) = 120" in output
    assert "factorial(10) = 3628800" in output
    assert "flatten(" in output
    assert "[1, 2, 3, 4, 5, 6, 7]" in output


def test_lambda_functions(capture_output: Callable) -> None:
    """Test lambda functions."""
    output = capture_output(lambda_functions)
    assert "Square of 5: 25" in output
    assert "Even numbers: [2, 4]" in output


def test_decorator_example(capture_output: Callable) -> None:
    """Test decorator functionality."""
    output = capture_output(decorator_example)
    assert "Function slow_function took" in output
    assert "Function slept for 0.5 seconds" in output
    assert "Hello, Python!" in output
