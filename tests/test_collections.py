"""Tests for collections module examples."""

from collections.abc import Callable

from pyquickref.examples.collections_ops import collections_example


def test_collections_example(capture_output: Callable) -> None:
    """Test collections module example."""
    output = capture_output(collections_example)
    assert "Counter" in output
    assert "Most common 2:" in output
    assert "defaultdict:" in output
    assert "namedtuple:" in output
    assert "deque" in output
