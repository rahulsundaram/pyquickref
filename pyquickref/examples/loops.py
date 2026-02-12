"""Loop examples for PyQuickRef.

This module contains examples demonstrating Python's loop constructs,
including for loops, while loops, enumerate, zip, and break/continue.
"""

from typing import Any


def loop_range(self: Any) -> None:
    """Demonstrate for loops with range, enumerate, and zip."""
    self.logger.info("Demonstrating loop constructs")

    # Basic range
    print("Range(5):", list(range(5)))

    # Enumerate — index + value
    fruits = ["apple", "banana", "cherry"]
    print("Enumerate:")
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")

    # Zip — iterate multiple sequences together
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    print("Zip:")
    for name, age in zip(names, ages, strict=False):
        print(f"  {name} is {age}")

    # While loop with break
    print("While loop (break at 3):")
    count = 0
    while count < 10:
        if count == 3:
            break
        print(f"  count={count}")
        count += 1

    # Continue — skip even numbers
    print("Continue (skip even):")
    for i in range(6):
        if i % 2 == 0:
            continue
        print(f"  {i}")
