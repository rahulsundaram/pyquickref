"""Tests for data structure operations."""

from collections.abc import Callable

from pyquickref.examples.data_structures import (
    basic_types,
    comprehensions,
    conditional_check,
    dict_iterate,
    list_comprehend,
    list_iterate,
    list_modify,
    references_copies,
    set_modify,
    slice_operations,
    star_unpacking,
    tuple_unpack,
)
from pyquickref.testdata import SampleData


def test_basic_types(capture_output: Callable) -> None:
    """Test basic types: int, float, bool, None, arithmetic, conversion."""
    output = capture_output(basic_types)
    assert "type: int" in output
    assert "type: float" in output
    assert "type: bool" in output
    assert "type: NoneType" in output
    assert "10 // 3 = 3" in output
    assert "2 ** 10 = 1024" in output
    assert 'int("42")  = 42' in output
    assert "isinstance(42, int)       = True" in output


def test_slice_operations(capture_output: Callable) -> None:
    """Test list and string slicing."""
    output = capture_output(slice_operations)
    assert "nums[2:5]  = [2, 3, 4]" in output
    assert "nums[:3]   = [0, 1, 2]" in output
    assert "nums[-3:]  = [7, 8, 9]" in output
    assert "nums[::2]  = [0, 2, 4, 6, 8]" in output
    assert "s[7:]   = 'World!'" in output


def test_comprehensions(capture_output: Callable) -> None:
    """Test dict, set, and generator comprehensions."""
    output = capture_output(comprehensions)
    assert "Dict comp:" in output
    assert "Passing:" in output
    assert "Alice" in output
    assert "Set comp:" in output
    assert "Gen expr sum of squares:" in output


def test_star_unpacking(capture_output: Callable) -> None:
    """Test star unpacking, dict merging, swap."""
    output = capture_output(star_unpacking)
    assert "first = 1, rest = [2, 3, 4, 5]" in output
    assert "middle = [2, 3, 4]" in output
    assert "Merged:" in output
    assert "'size': 'large'" in output
    assert "After swap: a=2, b=1" in output


def test_references_copies(capture_output: Callable) -> None:
    """Test object identity, mutability, and copying."""
    output = capture_output(references_copies)
    assert "a == b: True" in output
    assert "a is b: False" in output
    assert "a is c: True" in output
    assert "shallow:" in output
    assert "inner list shared" in output
    assert "fully independent" in output
    assert "bad_append(2) = [1, 2]" in output


def test_list_iterate(sample_data: SampleData, capture_output: Callable) -> None:
    """Test basic list iteration."""
    output = capture_output(list_iterate, sample_data)
    for item in ["apple", "banana", "cherry"]:
        assert item in output


def test_list_comprehend(capture_output: Callable) -> None:
    """Test list comprehension."""
    output = capture_output(list_comprehend)
    assert "[0,1,4,9,16]" in output.replace(" ", "")


def test_dict_iterate(sample_data: SampleData, capture_output: Callable) -> None:
    """Test dictionary operations."""
    output = capture_output(dict_iterate, sample_data)
    for key in ["a", "b", "c"]:
        assert f"Key: {key}" in output


def test_set_operations(sample_data: SampleData, capture_output: Callable) -> None:
    """Test set operations."""
    output = capture_output(set_modify, sample_data)
    assert "Original set:" in output
    assert "After adding 4:" in output
    assert "After removing 2:" in output


def test_list_modify(sample_data: SampleData, capture_output: Callable) -> None:
    """Test list modification operations."""
    output = capture_output(list_modify, sample_data)
    assert "Original list:" in output
    assert "After appending 'four':" in output
    assert "After removing 'banana':" in output
    assert "After reversing:" in output


def test_conditional_check(sample_data: SampleData, capture_output: Callable) -> None:
    """Test conditional check for item in list."""
    output = capture_output(conditional_check, sample_data)
    assert "'banana' is in the list!" in output


def test_tuple_unpacking(sample_data: SampleData, capture_output: Callable) -> None:
    """Test tuple unpacking."""
    output = capture_output(tuple_unpack, sample_data)
    assert "a=10, b=20, c=30" in output
