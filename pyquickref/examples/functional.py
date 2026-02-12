"""Functional programming examples for PyQuickRef.

Function basics, lambda functions, decorators, and higher-order functions.
Docs: https://docs.python.org/3/howto/functional.html
"""

import time
from collections.abc import Callable
from functools import wraps
from typing import Any

from pyquickref.registry import example, show


@example(
    "Functional",
    "def, default args, *args, **kwargs, return values",
    doc_url="https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
)
def function_basics() -> None:
    """Demonstrate function definitions, arguments, and return values."""

    def greet(name: str) -> str:
        """Return a greeting for the given name."""
        return f"Hello, {name}!"

    show(greet)
    print(greet("World"))

    def power(base: int, exp: int = 2) -> int:
        """Return base raised to exp (default: squared)."""
        return base**exp

    show(power)
    print(f"power(3)    = {power(3)}")
    print(f"power(3, 3) = {power(3, 3)}")

    def total(*args: int) -> int:
        """Return the sum of all arguments."""
        return sum(args)

    show(total)
    print(f"total(1, 2, 3) = {total(1, 2, 3)}")

    def build_url(base: str, **params: str) -> str:
        """Build a URL with query parameters from keyword arguments."""
        query = "&".join(f"{k}={v}" for k, v in params.items())
        return f"{base}?{query}" if query else base

    show(build_url)
    print(build_url("https://api.example.com", page="1", limit="10"))

    def min_max(items: list[int]) -> tuple[int, int]:
        """Return the min and max of a list as a tuple."""
        return min(items), max(items)

    show(min_max)
    lo, hi = min_max([3, 1, 4, 1, 5, 9])
    print(f"min={lo}, max={hi}")


@example(
    "Functional",
    "any(), all(), sorted(key=), min/max with key",
    doc_url="https://docs.python.org/3/library/functions.html",
)
def builtin_functions() -> None:
    """Demonstrate commonly-used builtin functions."""
    nums = [2, 4, 6, 8]
    show("nums = [2, 4, 6, 8]\nall(n % 2 == 0 for n in nums)")
    print(f"All even? {all(n % 2 == 0 for n in nums)}")
    print(f"Any > 5?  {any(n > 5 for n in nums)}")

    words = ["banana", "apple", "cherry", "date"]
    show("sorted(words, key=len)")
    print(f"By length: {sorted(words, key=len)}")

    show("sorted(words, key=str.lower, reverse=True)")
    print(f"Reverse alpha: {sorted(words, key=str.lower, reverse=True)}")

    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    show("min(people, key=lambda p: p[1])")
    youngest = min(people, key=lambda p: p[1])
    oldest = max(people, key=lambda p: p[1])
    print(f"Youngest: {youngest[0]} ({youngest[1]})")
    print(f"Oldest:   {oldest[0]} ({oldest[1]})")


@example(
    "Functional",
    "LEGB scope rule, global, nonlocal, closures",
    doc_url="https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces",
)
def scope_closures() -> None:
    """Demonstrate scope rules and closures."""
    x = "global"

    def outer() -> str:
        """Show LEGB scope resolution with nested functions."""
        x = "enclosing"

        def inner() -> str:
            x = "local"
            return x

        return f"inner={inner()}, enclosing={x}"

    show(outer)
    print(f"LEGB: {outer()}, global={x}")

    def counter() -> Callable[[], int]:
        """Return a closure that increments on each call."""
        count = 0

        def increment() -> int:
            nonlocal count
            count += 1
            return count

        return increment

    show(counter)
    c = counter()
    print(f"Closure: {c()}, {c()}, {c()}")

    def make_multiplier(factor: int) -> Callable[[int], int]:
        """Return a function that multiplies by factor."""
        return lambda x: x * factor

    show(make_multiplier)
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"double(5) = {double(5)}, triple(5) = {triple(5)}")


@example(
    "Functional",
    "Recursive functions: factorial, fibonacci, flatten",
    doc_url="https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
)
def recursion_example() -> None:
    """Demonstrate recursive functions."""

    def factorial(n: int) -> int:
        """Return n! using recursion."""
        return 1 if n <= 1 else n * factorial(n - 1)

    show(factorial)
    print(f"factorial(5) = {factorial(5)}")
    print(f"factorial(10) = {factorial(10)}")

    def flatten(lst: list[Any]) -> list[Any]:
        """Recursively flatten nested lists into a single list."""
        result: list[Any] = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    show(flatten)
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"flatten({nested}) = {flatten(nested)}")


@example(
    "Functional",
    "Lambda, map, filter, sorted with key functions",
    doc_url="https://docs.python.org/3/howto/functional.html",
)
def lambda_functions() -> None:
    """Demonstrate the use of lambda functions in Python."""
    square = lambda x: x**2
    result = square(5)
    show("square = lambda x: x**2\nsquare(5)")
    print(f"Square of 5: {result}")

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(square, numbers))
    show("list(map(square, [1, 2, 3, 4, 5]))")
    print(f"Original numbers: {numbers}")
    print(f"Squared (via map): {squared_numbers}")

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    show("list(filter(lambda x: x % 2 == 0, numbers))")
    print(f"Even numbers: {even_numbers}")

    people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
    sorted_by_age = sorted(people, key=lambda person: person[1])
    show("sorted(people, key=lambda person: person[1])")
    print(f"People sorted by age: {sorted_by_age}")


@example(
    "Functional",
    "Timer decorator and repeat decorator with arguments",
    doc_url="https://docs.python.org/3/glossary.html#term-decorator",
)
def decorator_example() -> None:
    """Demonstrate the use of decorators in Python."""

    def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """Print how long a function takes to run."""
        func_name = getattr(func, "__name__", repr(func))

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            print(f"Function {func_name} took {elapsed:.4f} seconds to run")
            return result

        return wrapper

    show(timer_decorator)

    @timer_decorator
    def slow_function(delay: float) -> str:
        time.sleep(delay)
        return f"Function slept for {delay} seconds"

    result = slow_function(0.5)
    print(result)

    def repeat(times: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """Repeat a function call n times, collecting results."""

        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> list[Any]:
                return [func(*args, **kwargs) for _ in range(times)]

            return wrapper

        return decorator

    show(repeat)

    @repeat(times=3)
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    results = greet("Python")
    print(results)
