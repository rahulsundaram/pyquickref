"""Tests for testing and debugging examples."""

from collections.abc import Callable

from pyquickref.examples.testing_debugging import debugging_example, pytest_example


def test_pytest_example(capture_output: Callable) -> None:
    """Test pytest patterns demonstration."""
    output = capture_output(pytest_example)
    assert "pytest.raises" in output
    assert "Fixtures provide setup/teardown" in output
    assert "PASS" in output
    assert "Markers:" in output
    assert "MagicMock" in output
    assert "mock.called = True" in output


def test_debugging_example(capture_output: Callable) -> None:
    """Test debugging tools demonstration."""
    output = capture_output(debugging_example)
    assert "breakpoint()" in output
    assert "PYTHONBREAKPOINT=0" in output
    assert "ZeroDivisionError" in output
    assert "assert isinstance(42, int) passed" in output
    assert "__debug__" in output
