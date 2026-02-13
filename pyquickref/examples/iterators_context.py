"""Iterator protocol and context manager examples for PyQuickRef.

Custom iterators, __iter__/__next__, with statement, contextlib.
Docs: https://docs.python.org/3/library/stdtypes.html#iterator-types
"""

import contextlib
import io

from pyquickref.registry import example, show


@example(
    "Iterators & Context Managers",
    "Iterator protocol: __iter__, __next__, StopIteration, custom iterators",
    doc_url="https://docs.python.org/3/library/stdtypes.html#iterator-types",
)
def iterator_protocol() -> None:
    """Demonstrate the iterator protocol with custom iterators."""

    class Countdown:
        """An iterator that counts down from n to 1."""

        def __init__(self, start: int) -> None:
            self.current = start

        def __iter__(self) -> "Countdown":
            return self

        def __next__(self) -> int:
            if self.current <= 0:
                raise StopIteration
            val = self.current
            self.current -= 1
            return val

    show(Countdown)
    print(f"Countdown(5): {list(Countdown(5))}")

    # iter() and next() builtins
    show("it = iter([10, 20, 30])\nnext(it)  # 10\nnext(it)  # 20")
    it = iter([10, 20, 30])
    print(f"next(it) = {next(it)}")
    print(f"next(it) = {next(it)}")
    print(f"next(it) = {next(it)}")

    # next() with default to avoid StopIteration
    show("next(it, 'done')  # returns default when exhausted")
    print(f"next(it, 'done') = {next(it, 'done')}")

    # Iterable vs iterator
    show(
        "# A list is iterable (has __iter__) but is NOT an iterator\n"
        "# iter(list) returns a list_iterator (has __next__)"
    )
    nums = [1, 2, 3]
    print(f"hasattr(list, '__iter__')     = {hasattr(nums, '__iter__')}")
    print(f"hasattr(list, '__next__')     = {hasattr(nums, '__next__')}")
    print(f"hasattr(iter(list), '__next__') = {hasattr(iter(nums), '__next__')}")


@example(
    "Iterators & Context Managers",
    "Context managers: with statement, __enter__/__exit__, custom CM",
    doc_url="https://docs.python.org/3/reference/datamodel.html#context-managers",
)
def context_manager_example() -> None:
    """Demonstrate the with statement and custom context managers."""

    class Timer:
        """A context manager that measures elapsed time."""

        def __init__(self, label: str) -> None:
            self.label = label
            self.elapsed: float = 0.0

        def __enter__(self) -> "Timer":
            import time

            self._start = time.monotonic()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb) -> bool:  # noqa: ANN001
            import time

            self.elapsed = time.monotonic() - self._start
            # Return False to propagate exceptions
            return False

    show(Timer)

    with Timer("demo") as t:
        total = sum(range(100_000))
    print(f"Timer elapsed: {t.elapsed:.4f}s (sum={total})")

    # __exit__ receives exception info
    class Suppressor:
        """Suppress a specific exception type."""

        def __init__(self, exc_type: type) -> None:
            self.exc_type = exc_type

        def __enter__(self) -> "Suppressor":
            return self

        def __exit__(self, exc_type, exc_val, exc_tb) -> bool:  # noqa: ANN001
            if exc_type is self.exc_type:
                print(f"  Suppressed {exc_type.__name__}: {exc_val}")
                return True  # Suppress the exception
            return False

    show(Suppressor)
    with Suppressor(ValueError):
        raise ValueError("test error")
    print("Continued after suppressed ValueError")


@example(
    "Iterators & Context Managers",
    "contextlib: @contextmanager, suppress, redirect_stdout",
    doc_url="https://docs.python.org/3/library/contextlib.html",
)
def contextlib_example() -> None:
    """Demonstrate contextlib utilities for writing context managers."""

    # @contextmanager turns a generator into a CM
    @contextlib.contextmanager
    def tag(name: str):  # noqa: ANN201, ANN202
        """Wrap output in XML-like tags."""
        print(f"<{name}>")
        yield name
        print(f"</{name}>")

    show(tag)
    with tag("body") as t:
        print(f"  content inside {t}")

    # suppress — cleaner than try/except for ignoring errors
    show("with contextlib.suppress(FileNotFoundError):\n    open('nonexistent.txt')")
    with contextlib.suppress(FileNotFoundError):
        open("nonexistent_file_12345.txt")  # noqa: SIM115
    print("suppress: FileNotFoundError silently ignored")

    # redirect_stdout — capture print output
    show("with contextlib.redirect_stdout(f):\n    print('captured')")
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        print("this is captured")
    print(f"redirect_stdout captured: {f.getvalue().strip()!r}")
