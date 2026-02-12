"""Tests for advanced features in PyQuickRef."""

from collections.abc import Callable
from typing import Any


def test_regex_patterns(quickref: Any, capture_output: Callable) -> None:
    """Test regular expressions."""
    output = capture_output(quickref.regex_patterns)
    assert "Emails found:" in output
    assert "info@example.com" in output
    assert "support@python.org" in output
    assert "Date found: 2023-11-25" in output


def test_json_operations(quickref: Any, capture_output: Callable) -> None:
    """Test JSON operations."""
    output = capture_output(quickref.json_operations)
    assert "John Doe" in output
    assert "First course: Python" in output


def test_thread_execute(quickref: Any, capture_output: Callable) -> None:
    """Test threading execution."""
    output = capture_output(quickref.thread_execute)
    for i in range(5):
        assert f"Task {i} completed" in output


def test_error_handling(quickref: Any, capture_output: Callable) -> None:
    """Test error handling with custom exceptions and multiple except."""
    output = capture_output(quickref.error_handle)
    assert "Caught ZeroDivisionError!" in output
    assert "Finally block always executes." in output
    assert "TypeError (unsupported type)" in output
    assert "Custom exception:" in output
    assert "Cannot withdraw $100.00" in output
