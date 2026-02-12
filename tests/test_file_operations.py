"""Tests for file operations."""

import os
from collections.abc import Callable

from pyquickref.examples.file_operations import context_managers, file_write


def test_file_write(output_dir: str, capture_output: Callable) -> None:
    """Test file writing."""
    output = capture_output(file_write, output_dir)
    assert "File written successfully" in output
    file_path = os.path.join(output_dir, "example.txt")
    assert os.path.exists(file_path)
    with open(file_path) as file:
        content = file.read()
    assert content == "Hello, file handling!"


def test_context_managers(output_dir: str, capture_output: Callable) -> None:
    """Test context managers."""
    output = capture_output(context_managers, output_dir)
    assert "File written with context manager" in output
    assert "Captured: Hello, context manager!" in output
    file_path = os.path.join(output_dir, "example_context.txt")
    assert os.path.exists(file_path)
    with open(file_path) as file:
        content = file.read()
    assert "Context managers automatically handle" in content
