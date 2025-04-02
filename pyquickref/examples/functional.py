"""Functional programming examples for PyQuickRef.

This module contains examples demonstrating Python's functional programming features,
including lambda functions, decorators, and higher-order functions.
"""

from functools import wraps
from typing import Any, Callable


def lambda_functions(self: Any) -> None:
    """Demonstrate the use of lambda functions in Python."""
    self.logger.info("Demonstrating lambda functions")
    # Simple lambda
    square = lambda x: x**2  # noqa: E731
    result = square(5)
    self.logger.debug(f"Lambda square result: {result}")
    print(f"Square of 5: {result}")

    # Lambda with list operations
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [x**2 for x in numbers]
    print(f"Original numbers: {numbers}")
    print(f"Squared numbers: {squared_numbers}")

    # Lambda with filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    self.logger.debug(f"Filtered even numbers: {even_numbers}")
    print(f"Even numbers: {even_numbers}")

    # Lambda with sorted
    people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
    sorted_by_age = sorted(people, key=lambda person: person[1])
    self.logger.debug(f"Sorted people by age: {sorted_by_age}")
    print(f"People sorted by age: {sorted_by_age}")


def decorator_example(self: Any) -> None:
    """Demonstrate the use of decorators in Python."""
    self.logger.info("Demonstrating Python decorators")

    # Define a decorator
    def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            import time

            self.logger.debug(f"Starting timing for {func.__name__}")
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed = end_time - start_time
            self.logger.info(
                f"Function {func.__name__} took {elapsed:.4f} seconds to run"
            )
            print(f"Function {func.__name__} took {elapsed:.4f} seconds to run")
            return result

        return wrapper

    # Apply the decorator to a function
    @timer_decorator
    def slow_function(delay: float) -> str:
        import time

        self.logger.debug(f"Sleeping for {delay} seconds")
        time.sleep(delay)
        return f"Function slept for {delay} seconds"

    result = slow_function(0.5)
    self.logger.debug(f"Result from slow_function: {result}")
    print(result)

    # Define a decorator with arguments
    def repeat(times: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> list[Any]:
                self.logger.debug(f"Repeating {func.__name__} {times} times")
                results = []
                for i in range(times):
                    self.logger.debug(f"Repeat {i + 1}/{times}")
                    results.append(func(*args, **kwargs))
                return results

            return wrapper

        return decorator

    # Apply the decorator with arguments
    @repeat(times=3)
    def greet(name: str) -> str:
        message = f"Hello, {name}!"
        self.logger.debug(f"Greeted {name}")
        return message

    results = greet("Python")
    self.logger.debug(f"Results from repeat decorator: {results}")
    print(results)
