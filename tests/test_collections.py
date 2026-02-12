"""Tests for collections module examples in PyQuickRef."""

from collections.abc import Callable
from typing import Any


def test_collections_example(quickref: Any, capture_output: Callable) -> None:
    """Test collections module example."""
    output = capture_output(quickref.collections_example)
    assert "Counter" in output
    assert "Most common 2:" in output
    assert "defaultdict:" in output
    assert "namedtuple:" in output
    assert "deque" in output
