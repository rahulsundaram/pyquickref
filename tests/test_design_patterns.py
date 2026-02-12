"""Tests for design pattern examples."""

from collections.abc import Callable

from pyquickref.examples.design_patterns import (
    factory_pattern,
    observer_pattern,
    strategy_pattern,
)


def test_factory_pattern(capture_output: Callable) -> None:
    """Test factory pattern creates correct notification types."""
    output = capture_output(factory_pattern)
    assert "Email: Hello!" in output
    assert "SMS: Hello!" in output
    assert "Push: Hello!" in output


def test_strategy_pattern(capture_output: Callable) -> None:
    """Test strategy pattern applies correct pricing."""
    output = capture_output(strategy_pattern)
    assert "full_price: $100.00" in output
    assert "ten_percent_off: $90.00" in output
    assert "member_discount: $80.00" in output


def test_observer_pattern(capture_output: Callable) -> None:
    """Test observer pattern emits events to listeners."""
    output = capture_output(observer_pattern)
    assert "Welcome, Alice!" in output
    assert "Audit: Alice logged in" in output
    assert "Goodbye, Alice!" in output
