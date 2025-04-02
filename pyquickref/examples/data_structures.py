"""Data structure examples for PyQuickRef.

This module contains examples demonstrating Python's data structures:
lists, dictionaries, sets, and tuples.
"""

from typing import Any


def list_iterate(self: Any) -> None:
    """Iterate through the list and print each item."""
    self.logger.info("Iterating through list")
    for item in self.testlist:
        print(item)


def conditional_check(self: Any) -> None:
    """Check if a specific item exists in the list and log the result."""
    self.logger.info("Checking for item in list")
    item = "banana"
    if item in self.testlist:
        self.logger.info(f"'{item}' is in the list!")
        print(f"'{item}' is in the list!")
    else:
        self.logger.info(f"'{item}' is not in the list.")
        print(f"'{item}' is not in the list.")


def list_modify(self: Any) -> None:
    """Modify the list by appending, removing, and reversing elements."""
    self.logger.info("Demonstrating list modifications")
    self.logger.debug(f"Original list: {self.testlist}")
    print("Original list:", self.testlist)

    self.testlist.append("four")
    self.logger.debug(f"After appending 'four': {self.testlist}")
    print("After appending 'four':", self.testlist)

    self.testlist.remove("banana")
    self.logger.debug(f"After removing 'banana': {self.testlist}")
    print("After removing 'banana':", self.testlist)

    self.testlist.reverse()
    self.logger.debug(f"After reversing: {self.testlist}")
    print("After reversing:", self.testlist)


def list_comprehend(self: Any) -> None:
    """Demonstrate list comprehension by creating a list of squares."""
    self.logger.info("Demonstrating list comprehension")
    squares = [x**2 for x in range(5)]
    self.logger.debug(f"Squares: {squares}")
    print("List comprehension (squares):", squares)


def dict_iterate(self: Any) -> None:
    """Iterate through the dictionary and print each key-value pair."""
    self.logger.info("Iterating through dictionary")
    for key, value in self.testdict.items():
        self.logger.debug(f"Dictionary entry - Key: {key}, Value: {value}")
        print(f"Key: {key}, Value: {value}")


def set_modify(self: Any) -> None:
    """Modify the set by adding and removing elements."""
    self.logger.info("Demonstrating set modifications")
    self.logger.debug(f"Original set: {self.testset}")
    print("Original set:", self.testset)

    self.testset.add(4)
    self.logger.debug(f"After adding 4: {self.testset}")
    print("After adding 4:", self.testset)

    self.testset.remove(2)
    self.logger.debug(f"After removing 2: {self.testset}")
    print("After removing 2:", self.testset)


def tuple_unpack(self: Any) -> None:
    """Unpack a tuple into individual variables and print them."""
    self.logger.info("Demonstrating tuple unpacking")
    a, b, c = self.testtuple
    self.logger.debug(f"Unpacked tuple values: a={a}, b={b}, c={c}")
    print(f"Unpacked tuple values: a={a}, b={b}, c={c}")
