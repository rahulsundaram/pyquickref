"""Tests for string operations."""

from collections.abc import Callable

from pyquickref.examples.strings import string_operations, unicode_bytes
from pyquickref.testdata import SampleData


def test_unicode_bytes(capture_output: Callable) -> None:
    """Test Unicode and bytes encoding/decoding."""
    output = capture_output(unicode_bytes)
    assert "type: str" in output
    assert "type: bytes" in output
    assert "decoded:" in output
    assert "utf-8 bytes:" in output
    assert "ascii:" in output


def test_string_operations(sample_data: SampleData, capture_output: Callable) -> None:
    """Test string operations."""
    output = capture_output(string_operations, sample_data)
    assert "Python is awesome" in output
    assert "PYTHON IS AWESOME" in output
    assert "Hello, World!" in output
