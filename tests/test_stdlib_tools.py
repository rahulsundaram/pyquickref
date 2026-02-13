"""Tests for stdlib tools examples."""

from collections.abc import Callable

from pyquickref.examples.stdlib_tools import (
    datetime_example,
    functools_example,
    logging_example,
    pathlib_example,
    subprocess_example,
)


def test_pathlib_example(capture_output: Callable) -> None:
    """Test pathlib operations."""
    output = capture_output(pathlib_example)
    assert "parent" in output
    assert "python3" in output
    assert "glob('*.txt')" in output


def test_datetime_example(capture_output: Callable) -> None:
    """Test datetime operations."""
    output = capture_output(datetime_example)
    assert "UTC now" in output
    assert "Tomorrow" in output
    assert "Formatted" in output
    assert "Parsed" in output


def test_functools_example(capture_output: Callable) -> None:
    """Test functools operations."""
    output = capture_output(functools_example)
    assert "fib(10) = 55" in output
    assert "cache_info" in output
    assert "double(5) = 10" in output
    assert "reduce sum = 15" in output


def test_logging_example(capture_output: Callable) -> None:
    """Test logging module demonstration."""
    output = capture_output(logging_example)
    assert "DEBUG" in output
    assert "INFO" in output
    assert "WARNING" in output
    assert "ERROR" in output


def test_subprocess_example(capture_output: Callable) -> None:
    """Test subprocess operations."""
    output = capture_output(subprocess_example)
    assert "'hello'" in output
    assert "returncode" in output
    assert "Command failed" in output
