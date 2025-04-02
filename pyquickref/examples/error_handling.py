"""Error handling examples for PyQuickRef.

This module contains examples demonstrating Python's error handling capabilities,
including try/except blocks, raising exceptions, and custom exceptions.
"""

from typing import Any


def error_handle(self: Any) -> None:
    """Demonstrate error handling with try-except-finally."""
    self.logger.info("Demonstrating error handling")
    try:
        self.logger.debug("Attempting division by zero")
        result = 10 / 0
        print(f"Result of division: {result}")  # This won't execute
    except ZeroDivisionError:
        self.logger.warning("Caught a division by zero error!")
        print("Caught a division by zero error!")
    finally:
        self.logger.debug("Executing finally block in error handling")
        print("This block always executes.")
