"""Tests for iterator and context manager examples."""

from collections.abc import Callable

from pyquickref.examples.iterators_context import (
    context_manager_example,
    contextlib_example,
    iterator_protocol,
)


def test_iterator_protocol(capture_output: Callable) -> None:
    """Test custom iterator and iter/next builtins."""
    output = capture_output(iterator_protocol)
    assert "Countdown(5): [5, 4, 3, 2, 1]" in output
    assert "next(it) = 10" in output
    assert "next(it, 'done') = done" in output
    assert "__iter__" in output
    assert "__next__" in output


def test_context_manager_example(capture_output: Callable) -> None:
    """Test custom context managers with __enter__/__exit__."""
    output = capture_output(context_manager_example)
    assert "Timer elapsed" in output
    assert "Suppressed ValueError" in output
    assert "Continued after suppressed ValueError" in output


def test_contextlib_example(capture_output: Callable) -> None:
    """Test contextlib utilities."""
    output = capture_output(contextlib_example)
    assert "<body>" in output
    assert "</body>" in output
    assert "content inside body" in output
    assert "FileNotFoundError silently ignored" in output
    assert "redirect_stdout captured" in output
