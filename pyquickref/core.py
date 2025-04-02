"""Core functionality for PyQuickRef.

This module defines the PyQuickRef class which serves as the main entry point
for running Python examples and demonstrations.
"""

import logging
import os
from typing import Any, Callable, Optional

# Import all the example methods first
from pyquickref.examples.advanced import (
    itertools_examples,
    json_operations,
    regex_patterns,
    thread_execute,
)
from pyquickref.examples.data_structures import (
    conditional_check,
    dict_iterate,
    list_comprehend,
    list_iterate,
    list_modify,
    set_modify,
    tuple_unpack,
)
from pyquickref.examples.error_handling import error_handle
from pyquickref.examples.file_operations import (
    context_managers,
    file_write,
)
from pyquickref.examples.functional import (
    decorator_example,
    lambda_functions,
)
from pyquickref.examples.loops import loop_range
from pyquickref.examples.strings import string_operations


class PyQuickRef:
    """A utility class that demonstrates various Python concepts and operations.

    Includes data structures, file handling, JSON handling, threading, and more.
    """

    def run_examples(
        self: "PyQuickRef", functions_to_run: Optional[list[str]] = None
    ) -> None:
        """Run specified examples or all examples if none are specified.

        Args:
        ----
            functions_to_run: Optional list of function names to run.
                If None or empty list, run all examples.

        """
        available_methods = {
            method_name: method
            for method_name, method in vars(PyQuickRef).items()
            if callable(method) and not method_name.startswith("_")
        }
        if functions_to_run:
            for func in functions_to_run:
                if func in available_methods:
                    self.logger.info(f"Running example: {func}")
                    available_methods[func](self)
                else:
                    self.logger.warning(f"Function '{func}' not found in PyQuickRef.")
        else:
            self.logger.info("Running all examples.")
            for method_name, method in available_methods.items():
                if not method_name.startswith("_") and method_name != "run_examples":
                    self.logger.info(f"Running example: {method_name}")
                    method(self)

    def __init__(
        self: "PyQuickRef", logger: logging.Logger, output_dir: Optional[str] = None
    ) -> None:
        """Initialize the PyQuickRef instance.

        Args:
        ----
            logger (logging.Logger): Logger instance for logging messages.
            output_dir (Optional[str]): Directory for output files. Defaults to None.

        """
        self.logger = logger
        self.output_dir = output_dir or "data"  # Updated default directory

        # Initialize test data
        self.testlist: list[str] = ["apple", "banana", "cherry"]
        self.testdict: dict[str, int] = {"a": 1, "b": 2, "c": 3}
        self.testset: set[int] = {1, 2, 3}
        self.testtuple: tuple[int, int, int] = (10, 20, 30)
        self.teststring: str = "Python is awesome!"

        if self.output_dir and not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            self.logger.info(f"Created output directory: {self.output_dir}")

    def _get_output_path(self: "PyQuickRef", filename: str) -> str:
        """Generate the full output path for a given filename.

        Args:
        ----
            filename (str): The name of the file.

        Returns:
        -------
            str: The full path to the output file.

        """
        if self.output_dir:
            return os.path.join(self.output_dir, filename)
        else:
            self.logger.warning("Output directory is not set. Returning filename only.")
            return filename

    # Define attribute types to satisfy type checking
    list_iterate: Callable[[Any], None]
    list_modify: Callable[[Any], None]
    list_comprehend: Callable[[Any], None]
    dict_iterate: Callable[[Any], None]
    set_modify: Callable[[Any], None]
    tuple_unpack: Callable[[Any], None]
    conditional_check: Callable[[Any], None]
    string_operations: Callable[[Any], None]
    lambda_functions: Callable[[Any], None]
    decorator_example: Callable[[Any], None]
    file_write: Callable[[Any], None]
    context_managers: Callable[[Any], None]
    error_handle: Callable[[Any], None]
    json_operations: Callable[[Any], None]
    regex_patterns: Callable[[Any], None]
    itertools_examples: Callable[[Any], None]
    thread_execute: Callable[[Any], None]
    loop_range: Callable[[Any], None]


# Add the method implementations to the PyQuickRef class
PyQuickRef.list_iterate = list_iterate
PyQuickRef.list_modify = list_modify
PyQuickRef.list_comprehend = list_comprehend
PyQuickRef.dict_iterate = dict_iterate
PyQuickRef.set_modify = set_modify
PyQuickRef.tuple_unpack = tuple_unpack
PyQuickRef.conditional_check = conditional_check
PyQuickRef.string_operations = string_operations
PyQuickRef.lambda_functions = lambda_functions
PyQuickRef.decorator_example = decorator_example
PyQuickRef.file_write = file_write
PyQuickRef.context_managers = context_managers
PyQuickRef.error_handle = error_handle
PyQuickRef.json_operations = json_operations
PyQuickRef.regex_patterns = regex_patterns
PyQuickRef.itertools_examples = itertools_examples
PyQuickRef.thread_execute = thread_execute
PyQuickRef.loop_range = loop_range
