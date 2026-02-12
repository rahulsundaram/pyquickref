"""Tests for data structure operations in PyQuickRef."""

from collections.abc import Callable
from typing import Any


def test_list_iterate(quickref: Any, capture_output: Callable) -> None:
    """Test basic list iteration."""
    output = capture_output(quickref.list_iterate)
    for item in ["apple", "banana", "cherry"]:
        assert item in output


def test_list_comprehend(quickref: Any, capture_output: Callable) -> None:
    """Test list comprehension."""
    output = capture_output(quickref.list_comprehend)
    # Remove all spaces for comparison to handle formatting differences
    assert "[0,1,4,9,16]" in output.replace(" ", "")


def test_dict_iterate(quickref: Any, capture_output: Callable) -> None:
    """Test dictionary operations."""
    output = capture_output(quickref.dict_iterate)
    for key in ["a", "b", "c"]:
        assert f"Key: {key}" in output


def test_set_operations(quickref: Any, capture_output: Callable) -> None:
    """Test set operations."""
    output = capture_output(quickref.set_modify)
    assert "Original set:" in output
    assert "After adding 4:" in output
    assert "After removing 2:" in output


def test_list_modify(quickref: Any, capture_output: Callable) -> None:
    """Test list modification operations."""
    output = capture_output(quickref.list_modify)
    assert "Original list:" in output
    assert "After appending 'four':" in output
    assert "After removing 'banana':" in output
    assert "After reversing:" in output


def test_conditional_check(quickref: Any, capture_output: Callable) -> None:
    """Test conditional check for item in list."""
    output = capture_output(quickref.conditional_check)
    assert "'banana' is in the list!" in output


def test_tuple_unpacking(quickref: Any, capture_output: Callable) -> None:
    """Test tuple unpacking."""
    output = capture_output(quickref.tuple_unpack)
    assert "a=10, b=20, c=30" in output
