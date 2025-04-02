"""Tests for data structure operations in PyQuickRef."""

from typing import Any, Callable


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
    # Remove all spaces for comparison to handle formatting differences
    assert "Originalset:{1,2,3}" in output.replace(" ", "")
    assert "After adding 4:" in output
    assert "After removing 2:" in output


def test_tuple_unpacking(quickref: Any, capture_output: Callable) -> None:
    """Test tuple unpacking."""
    output = capture_output(quickref.tuple_unpack)
    assert "a=10, b=20, c=30" in output
