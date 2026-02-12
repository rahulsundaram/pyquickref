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

    # Basic function
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    show("def greet(name):\n    return f'Hello, {name}!'")
    print(greet("World"))

    # Default arguments
    def power(base: int, exp: int = 2) -> int:
        return base**exp

    show("def power(base, exp=2):\n    return base ** exp")
    print(f"power(3)    = {power(3)}")
    print(f"power(3, 3) = {power(3, 3)}")

    # *args — variable positional arguments
    def total(*args: int) -> int:
        return sum(args)

    show("def total(*args):\n    return sum(args)")
    print(f"total(1, 2, 3) = {total(1, 2, 3)}")

    # **kwargs — variable keyword arguments
    def build_url(base: str, **params: str) -> str:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        return f"{base}?{query}" if query else base

    show(
        "def build_url(base, **params):\n"
        "    query = '&'.join(f'{k}={v}' for k, v in params.items())\n"
        "    return f'{base}?{query}'"
    )
    print(build_url("https://api.example.com", page="1", limit="10"))

    # Multiple return values
    def min_max(items: list[int]) -> tuple[int, int]:
        return min(items), max(items)

    show("def min_max(items):\n    return min(items), max(items)")
    lo, hi = min_max([3, 1, 4, 1, 5, 9])
    print(f"min={lo}, max={hi}")


@example(
    "Functional",
    "any(), all(), sorted(key=), min/max with key",
    doc_url="https://docs.python.org/3/library/functions.html",
)
def builtin_functions() -> None:
    """Demonstrate commonly-used builtin functions."""
    # any / all
    nums = [2, 4, 6, 8]
    show("nums = [2, 4, 6, 8]\nall(n % 2 == 0 for n in nums)")
    print(f"All even? {all(n % 2 == 0 for n in nums)}")
    print(f"Any > 5?  {any(n > 5 for n in nums)}")

    # sorted with key
    words = ["banana", "apple", "cherry", "date"]
    show("sorted(words, key=len)")
    print(f"By length: {sorted(words, key=len)}")

    show("sorted(words, key=str.lower, reverse=True)")
    print(f"Reverse alpha: {sorted(words, key=str.lower, reverse=True)}")

    # min/max with key
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
    # LEGB: Local, Enclosing, Global, Built-in
    x = "global"

    def outer() -> str:
        x = "enclosing"

        def inner() -> str:
            x = "local"
            return x

        return f"inner={inner()}, enclosing={x}"

    show(
        "x = 'global'\n"
        "def outer():\n"
        "    x = 'enclosing'\n"
        "    def inner():\n"
        "        x = 'local'\n"
        "        return x"
    )
    print(f"LEGB: {outer()}, global={x}")

    # nonlocal — modify enclosing scope
    def counter() -> Callable[[], int]:
        count = 0

        def increment() -> int:
            nonlocal count
            count += 1
            return count

        return increment

    show(
        "def counter():\n"
        "    count = 0\n"
        "    def increment():\n"
        "        nonlocal count\n"
        "        count += 1\n"
        "        return count\n"
        "    return increment"
    )
    c = counter()
    print(f"Closure: {c()}, {c()}, {c()}")

    # Closure capturing a variable
    def make_multiplier(factor: int) -> Callable[[int], int]:
        return lambda x: x * factor

    show("def make_multiplier(factor):\n    return lambda x: x * factor")
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
        return 1 if n <= 1 else n * factorial(n - 1)

    show("def factorial(n):\n    return 1 if n <= 1 else n * factorial(n - 1)")
    print(f"factorial(5) = {factorial(5)}")
    print(f"factorial(10) = {factorial(10)}")

    # Recursive flatten
    def flatten(lst: list[Any]) -> list[Any]:
        result: list[Any] = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    show(
        "def flatten(lst):\n"
        "    result = []\n"
        "    for item in lst:\n"
        "        if isinstance(item, list):\n"
        "            result.extend(flatten(item))\n"
        "        else:\n"
        "            result.append(item)\n"
        "    return result"
    )
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"flatten({nested}) = {flatten(nested)}")


@example(
    "Functional",
    "Lambda, map, filter, sorted with key functions",
    doc_url="https://docs.python.org/3/howto/functional.html",
)
def lambda_functions() -> None:
    """Demonstrate the use of lambda functions in Python."""
    # Simple lambda
    square = lambda x: x**2
    result = square(5)
    show("square = lambda x: x**2\nsquare(5)")
    print(f"Square of 5: {result}")

    # Map with a callable
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(square, numbers))
    show("list(map(square, [1, 2, 3, 4, 5]))")
    print(f"Original numbers: {numbers}")
    print(f"Squared (via map): {squared_numbers}")

    # Lambda with filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    show("list(filter(lambda x: x % 2 == 0, numbers))")
    print(f"Even numbers: {even_numbers}")

    # Lambda with sorted
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

    # Define a decorator
    def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        func_name = getattr(func, "__name__", repr(func))

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            print(f"Function {func_name} took {elapsed:.4f} seconds to run")
            return result

        return wrapper

    show("@timer_decorator\ndef slow_function(delay):\n    time.sleep(delay)")

    @timer_decorator
    def slow_function(delay: float) -> str:
        time.sleep(delay)
        return f"Function slept for {delay} seconds"

    result = slow_function(0.5)
    print(result)

    # Decorator with arguments
    def repeat(times: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> list[Any]:
                return [func(*args, **kwargs) for _ in range(times)]

            return wrapper

        return decorator

    show("@repeat(times=3)\ndef greet(name):\n    return f'Hello, {name}!'")

    @repeat(times=3)
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    results = greet("Python")
    print(results)
