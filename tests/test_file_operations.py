"""Tests for file operations in PyQuickRef."""

import os
from collections.abc import Callable
from typing import Any


def test_file_write(quickref: Any, capture_output: Callable, temp_dir: str) -> None:
    """Test file writing."""
    output = capture_output(quickref.file_write)
    assert "File written successfully" in output
    # Check that the file was created in output directory
    file_path = os.path.join(temp_dir, "output", "example.txt")
    assert os.path.exists(file_path)
    with open(file_path) as file:
        content = file.read()
    assert content == "Hello, file handling!"


def test_context_managers(
    quickref: Any, capture_output: Callable, temp_dir: str
) -> None:
    """Test context managers."""
    output = capture_output(quickref.context_managers)
    assert "File written with context manager" in output
    assert "Captured: Hello, context manager!" in output
    # Check that the file was created
    file_path = os.path.join(temp_dir, "output", "example_context.txt")
    assert os.path.exists(file_path)
    with open(file_path) as file:
        content = file.read()
    assert "Context managers automatically handle" in content
