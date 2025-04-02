"""Tests for advanced features in PyQuickRef."""

from typing import Any, Callable


def test_regex_patterns(quickref: Any, capture_output: Callable) -> None:
    """Test regular expressions."""
    output = capture_output(quickref.regex_patterns)
    # The exact content may depend on the regex_test.txt file
    assert "info@example.com" in output or "support@python.org" in output
    assert "Date found:" in output or "Emails found:" in output


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
    """Test error handling."""
    output = capture_output(quickref.error_handle)
    assert "Caught a division by zero error!" in output
    assert "This block always executes" in output
