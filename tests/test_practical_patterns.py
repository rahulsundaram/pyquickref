"""Tests for practical pattern examples."""

from collections.abc import Callable

from pyquickref.examples.practical_patterns import (
    batch_processing,
    config_cascade,
    groupby_aggregate,
    guard_clauses,
    immutable_data,
    memoize_pattern,
    pipeline_pattern,
    retry_backoff,
    timeout_wrapper,
)


def test_retry_backoff(capture_output: Callable) -> None:
    """Test retry with exponential backoff."""
    output = capture_output(retry_backoff)
    assert "Attempt 1 failed" in output
    assert "Attempt 2 failed" in output
    assert "Result: success" in output


def test_timeout_wrapper(capture_output: Callable) -> None:
    """Test timeout decorator."""
    output = capture_output(timeout_wrapper)
    assert "Fast: fast result" in output
    assert "Timed out after" in output


def test_pipeline_pattern(capture_output: Callable) -> None:
    """Test function composition pipeline."""
    output = capture_output(pipeline_pattern)
    assert "'John Doe'" in output
    assert "sum = 45" in output


def test_batch_processing(capture_output: Callable) -> None:
    """Test batch processing with chunks."""
    output = capture_output(batch_processing)
    assert "Batch 1:" in output
    assert "Batch 4:" in output
    assert "sum=" in output


def test_groupby_aggregate(capture_output: Callable) -> None:
    """Test groupby and aggregation."""
    output = capture_output(groupby_aggregate)
    assert "North:" in output
    assert "South:" in output
    assert "total=$" in output


def test_config_cascade(capture_output: Callable) -> None:
    """Test config cascade with ChainMap."""
    output = capture_output(config_cascade)
    assert "host:" in output
    assert "localhost" in output
    assert "debug:   True" in output


def test_guard_clauses(capture_output: Callable) -> None:
    """Test guard clause pattern."""
    output = capture_output(guard_clauses)
    assert "error: no user" in output
    assert "is inactive" in output
    assert "is unverified" in output
    assert "is underage" in output
    assert "Diana is valid" in output


def test_immutable_data(capture_output: Callable) -> None:
    """Test frozen dataclass and NamedTuple."""
    output = capture_output(immutable_data)
    assert "Point(x=3.0, y=4.0)" in output
    assert "AttributeError (frozen!)" in output
    assert "Color" in output
    assert "Equal by value: True" in output


def test_memoize_pattern(capture_output: Callable) -> None:
    """Test memoization with lru_cache and manual cache."""
    output = capture_output(memoize_pattern)
    assert "fib(30) =" in output
    assert "not 2^30" in output
    assert "hits=" in output
    assert "Manual cache:" in output
