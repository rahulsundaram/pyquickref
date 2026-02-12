"""File operation examples for PyQuickRef.

This module contains examples demonstrating Python's file operations,
including reading, writing, and context managers.
"""

import contextlib
import io
from collections.abc import Iterator
from typing import Any


def file_write(self: Any) -> None:
    """Write a sample message to a file in the output directory."""
    self.logger.info("Demonstrating file writing")
    try:
        output_path = self._get_output_path("example.txt")
        self.logger.debug(f"Opening {output_path} for writing")
        with open(output_path, "w") as file:
            file.write("Hello, file handling!")
        self.logger.info("File written successfully.")
        print(f"File written successfully to {output_path}")
    except OSError as e:
        self.logger.error(f"Error writing to file: {e}")


def context_managers(self: Any) -> None:
    """Demonstrate the use of context managers in Python."""
    self.logger.info("Demonstrating context managers")
    try:
        output_path = self._get_output_path("example_context.txt")
        with open(output_path, "w") as file:
            file.write("Context managers automatically handle resource cleanup")
        self.logger.info("File written with context manager")
        print(f"File written with context manager to {output_path}")
    except OSError as e:
        self.logger.error(f"Error writing to file: {e}")

    # Custom context manager using contextlib
    @contextlib.contextmanager
    def string_io() -> Iterator[io.StringIO]:
        output = io.StringIO()
        try:
            yield output
        finally:
            value = output.getvalue()
            output.close()
            self.logger.debug(f"Captured in StringIO: {value}")
            print(f"Captured: {value}")

    self.logger.debug("Using custom string_io context manager")
    with string_io() as s:
        s.write("Hello, context manager!")
