"""Tests for advanced features."""

from collections.abc import Callable

from pyquickref.examples.advanced import (
    itertools_examples,
    regex_patterns,
    thread_execute,
)
from pyquickref.examples.error_handling import error_handle


def test_regex_patterns(capture_output: Callable) -> None:
    """Test regular expressions."""
    output = capture_output(regex_patterns)
    assert "Emails found:" in output
    assert "info@example.com" in output
    assert "support@python.org" in output
    assert "Date found: 2023-11-25" in output


def test_thread_execute(capture_output: Callable) -> None:
    """Test threading execution."""
    output = capture_output(thread_execute)
    for i in range(5):
        assert f"Task {i} completed" in output


def test_error_handling(capture_output: Callable) -> None:
    """Test error handling with custom exceptions and multiple except."""
    output = capture_output(error_handle)
    assert "Caught ZeroDivisionError!" in output
    assert "Finally block always executes." in output
    assert "TypeError (unsupported type)" in output
    assert "Custom exception:" in output
    assert "Cannot withdraw $100.00" in output


def test_itertools_examples(capture_output: Callable) -> None:
    """Test itertools functionality."""
    output = capture_output(itertools_examples)
    assert "('A', 'B')" in output
    assert "Cycling through colors" in output
