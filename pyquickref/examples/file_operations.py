"""File operation examples for PyQuickRef.

Reading, writing, and context managers.
Docs: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

import contextlib
import io
import os
from collections.abc import Iterator

from pyquickref.registry import example, show


@example(
    "File Operations",
    "Write text to a file using open()",
    doc_url="https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files",
    needs_output_dir=True,
)
def file_write(output_dir: str) -> None:
    """Write a sample message to a file in the output directory."""
    output_path = os.path.join(output_dir, "example.txt")
    show("with open('example.txt', 'w') as f:\n    f.write('Hello, file handling!')")
    try:
        with open(output_path, "w") as file:
            file.write("Hello, file handling!")
        print(f"File written successfully to {output_path}")
    except OSError as e:
        print(f"Error writing to file: {e}")


@example(
    "File Operations",
    "Context managers (with statement) and custom context managers",
    doc_url="https://docs.python.org/3/library/contextlib.html",
    needs_output_dir=True,
)
def context_managers(output_dir: str) -> None:
    """Demonstrate the use of context managers in Python."""
    output_path = os.path.join(output_dir, "example_context.txt")
    show("with open('example_context.txt', 'w') as f:\n    f.write('...')")
    try:
        with open(output_path, "w") as file:
            file.write("Context managers automatically handle resource cleanup")
        print(f"File written with context manager to {output_path}")
    except OSError as e:
        print(f"Error writing to file: {e}")

    # Custom context manager using contextlib
    show(
        "@contextlib.contextmanager\n"
        "def string_io():\n"
        "    output = io.StringIO()\n"
        "    try:\n        yield output\n"
        "    finally:\n        print(output.getvalue())"
    )

    @contextlib.contextmanager
    def string_io() -> Iterator[io.StringIO]:
        output = io.StringIO()
        try:
            yield output
        finally:
            value = output.getvalue()
            output.close()
            print(f"Captured: {value}")

    with string_io() as s:
        s.write("Hello, context manager!")
