"""Loop examples for PyQuickRef.

This module contains examples demonstrating Python's loop constructs,
including for loops, while loops, and comprehensions.
"""

from typing import Any


def loop_range(self: Any) -> None:
    """Demonstrate looping through a range and printing each item."""
    self.logger.info("Demonstrating range loop")
    self.logger.debug("Looping through range(1, 10)")
    for item in range(1, 10):
        print(item)
