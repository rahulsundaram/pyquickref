"""Error handling examples for PyQuickRef.

Try/except blocks, raising exceptions, and custom exceptions.
Docs: https://docs.python.org/3/tutorial/errors.html
"""

from pyquickref.registry import example, show


class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance."""

    def __init__(self: "InsufficientFundsError", balance: float, amount: float) -> None:
        """Initialize with current balance and requested withdrawal amount."""
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount:.2f}, balance is ${balance:.2f}")


@example(
    "Error Handling",
    "try/except/finally, multiple except, custom exceptions",
    doc_url="https://docs.python.org/3/tutorial/errors.html",
)
def error_handle() -> None:
    """Demonstrate error handling with try-except-finally and custom exceptions."""
    # Basic try/except/finally
    show(
        "try:\n    result = 10 / 0\n"
        "except ZeroDivisionError:\n    print('Caught!')\n"
        "finally:\n    print('Always runs')"
    )
    try:
        result = 10 / 0
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError!")
    finally:
        print("Finally block always executes.")

    # Multiple except clauses
    show("try:\n    100 / val\nexcept ZeroDivisionError: ...\nexcept TypeError: ...")
    values = [1, "two", None]
    for val in values:
        try:
            print(f"  100 / {val!r} = {100 / val}")  # type: ignore[operator]
        except ZeroDivisionError:
            print(f"  100 / {val!r} = ZeroDivisionError")
        except TypeError:
            print(f"  100 / {val!r} = TypeError (unsupported type)")

    # Custom exception
    show(InsufficientFundsError)
    balance = 50.0
    try:
        amount = 100.0
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
    except InsufficientFundsError as e:
        print(f"Custom exception: {e}")
