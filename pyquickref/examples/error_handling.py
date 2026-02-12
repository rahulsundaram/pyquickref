"""Error handling examples for PyQuickRef.

This module contains examples demonstrating Python's error handling capabilities,
including try/except blocks, raising exceptions, and custom exceptions.
"""

from typing import Any


class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance."""

    def __init__(self: "InsufficientFundsError", balance: float, amount: float) -> None:
        """Initialize with current balance and requested withdrawal amount."""
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount:.2f}, balance is ${balance:.2f}")


def error_handle(self: Any) -> None:
    """Demonstrate error handling with try-except-finally and custom exceptions."""
    self.logger.info("Demonstrating error handling")

    # Basic try/except/finally
    try:
        result = 10 / 0
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError!")
    finally:
        print("Finally block always executes.")

    # Multiple except clauses
    values = [1, "two", None]
    for val in values:
        try:
            print(f"  100 / {val!r} = {100 / val}")  # type: ignore[operator]
        except ZeroDivisionError:
            print(f"  100 / {val!r} = ZeroDivisionError")
        except TypeError:
            print(f"  100 / {val!r} = TypeError (unsupported type)")

    # Custom exception
    balance = 50.0
    try:
        amount = 100.0
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
    except InsufficientFundsError as e:
        print(f"Custom exception: {e}")
