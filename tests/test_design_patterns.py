"""Tests for design pattern examples."""

from collections.abc import Callable

from pyquickref.examples.design_patterns import (
    builder_pattern,
    factory_pattern,
    observer_pattern,
    producer_consumer,
    rate_limiter,
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


def test_builder_pattern(capture_output: Callable) -> None:
    """Test builder pattern creates HTTP request."""
    output = capture_output(builder_pattern)
    assert "POST https://api.example.com/users" in output
    assert "Content-Type" in output
    assert "Authorization" in output
    assert '{"name": "Alice"}' in output
    assert "Timeout: 10.0s" in output


def test_producer_consumer(capture_output: Callable) -> None:
    """Test producer/consumer with queue."""
    output = capture_output(producer_consumer)
    assert "Produced: [1, 2, 3, 4, 5]" in output
    assert "Consumed:" in output
    assert "Queue empty: True" in output


def test_rate_limiter(capture_output: Callable) -> None:
    """Test token bucket rate limiter."""
    output = capture_output(rate_limiter)
    assert "allowed" in output
    assert "denied" in output
    assert "rate limited" in output
