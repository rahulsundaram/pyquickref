"""String operation examples for PyQuickRef.

This module contains examples demonstrating Python's string operations,
including string manipulation, formatting, and methods.
"""

from typing import Any


def string_operations(self: Any) -> None:
    """Perform various string operations and demonstrate their usage."""
    self.logger.info("Demonstrating string operations")
    # Basic operations
    self.logger.debug(f"Original string: '{self.teststring}'")
    print(f"Original string: '{self.teststring}'")

    upper_case = self.teststring.upper()
    self.logger.debug(f"Uppercase: '{upper_case}'")
    print(f"Uppercase: '{upper_case}'")

    lower_case = self.teststring.lower()
    self.logger.debug(f"Lowercase: '{lower_case}'")
    print(f"Lowercase: '{lower_case}'")

    split_result = self.teststring.split()
    self.logger.debug(f"Split by space: {split_result}")
    print(f"Split by space: {split_result}")

    replaced = self.teststring.replace("awesome", "amazing")
    self.logger.debug(f"Replace: '{replaced}'")
    print(f"Replace: '{replaced}'")

    contains = "Python" in self.teststring
    self.logger.debug(f"Contains 'Python': {contains}")
    print(f"Contains 'Python': {contains}")

    # String formatting
    self.logger.info("Demonstrating string formatting")
    name = "World"
    # f-strings (Python 3.6+)
    self.logger.debug(f"f-string example: Hello, {name}!")
    print(f"Hello, {name}!")
    # format method
    formatted = f"Hello, {name}!"
    self.logger.debug(f"format() example: {formatted}")
    print(formatted)
    # format with multiple parameters
    multi_formatted = "The {animal} is {color}".format(animal="fox", color="brown")
    self.logger.debug(f"Multi-parameter format example: {multi_formatted}")
    print(multi_formatted)
