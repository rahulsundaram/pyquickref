"""Example registry for PyQuickRef.

Decorators and helpers for registering and discovering examples.
"""

from collections.abc import Callable
from dataclasses import dataclass, field
from types import FunctionType
from typing import Any


@dataclass
class ExampleInfo:
    """Metadata about a registered example function."""

    func: Callable[..., None]
    name: str
    category: str
    description: str
    doc_url: str = ""
    needs_test_data: bool = False
    needs_output_dir: bool = False
    tags: list[str] = field(default_factory=list)


@dataclass
class Lesson:
    """A lesson groups related categories into a learning unit."""

    number: int
    title: str
    goal: str
    categories: list[str]
    doc_url: str = ""


# Ordered progression from beginner to advanced.
LESSONS: list[Lesson] = [
    Lesson(
        1,
        "Data Structures",
        "Types, lists, dicts, sets, tuples, slicing, comprehensions",
        ["Data Structures"],
        doc_url="https://docs.python.org/3/tutorial/datastructures.html",
    ),
    Lesson(
        2,
        "Strings & Control Flow",
        "if/elif/else, for/while loops, string manipulation",
        ["Control Flow", "Strings", "Loops"],
        doc_url="https://docs.python.org/3/tutorial/controlflow.html",
    ),
    Lesson(
        3,
        "Functions",
        "def, args, kwargs, lambda, map, filter, decorators, builtins",
        ["Functional"],
        doc_url="https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
    ),
    Lesson(
        4,
        "Classes & OOP",
        "Classes, inheritance, properties, dunder methods",
        ["Classes"],
        doc_url="https://docs.python.org/3/tutorial/classes.html",
    ),
    Lesson(
        5,
        "Error Handling",
        "try/except/finally, custom exceptions, defensive coding",
        ["Error Handling"],
        doc_url="https://docs.python.org/3/tutorial/errors.html",
    ),
    Lesson(
        6,
        "Collections & Itertools",
        "Counter, defaultdict, deque, combinations, permutations",
        ["Collections"],
        doc_url="https://docs.python.org/3/library/collections.html",
    ),
    Lesson(
        7,
        "File I/O & Data Formats",
        "File read/write, context managers, JSON, regex",
        ["File Operations", "Advanced"],
        doc_url="https://docs.python.org/3/tutorial/inputoutput.html",
    ),
    Lesson(
        8,
        "Modern Python",
        "Dataclasses, pattern matching, generators, enums, type hints",
        ["Modern Python"],
        doc_url="https://docs.python.org/3/whatsnew/3.10.html",
    ),
    Lesson(
        9,
        "Standard Library",
        "pathlib, datetime, functools — batteries included",
        ["Stdlib Tools"],
        doc_url="https://docs.python.org/3/library/index.html",
    ),
    Lesson(
        10,
        "Design Patterns",
        "Factory, strategy, observer, builder, producer/consumer, rate limiter",
        ["Design Patterns"],
        doc_url="https://refactoring.guru/design-patterns/python",
    ),
    Lesson(
        11,
        "Practical Patterns",
        "Retry, timeout, pipeline, batching — real-world utilities",
        ["Practical Patterns"],
        doc_url="https://docs.python.org/3/library/functools.html",
    ),
]


_REGISTRY: dict[str, ExampleInfo] = {}

# The decorator accepts and returns FunctionType (def functions with __name__),
# but we widen the return so decorated functions still type as Callable.
_F = Callable[..., None]


def example(
    category: str,
    description: str,
    *,
    doc_url: str = "",
    needs_test_data: bool = False,
    needs_output_dir: bool = False,
    tags: list[str] | None = None,
) -> Callable[[_F], _F]:
    """Register a function as a runnable example."""

    def decorator(func: _F) -> _F:
        assert isinstance(func, FunctionType)
        _REGISTRY[func.__name__] = ExampleInfo(
            func=func,
            name=func.__name__,
            category=category,
            description=description,
            doc_url=doc_url,
            needs_test_data=needs_test_data,
            needs_output_dir=needs_output_dir,
            tags=tags or [],
        )
        return func

    return decorator


def get_registry() -> dict[str, ExampleInfo]:
    """Return all registered examples."""
    return _REGISTRY


def get_by_category() -> dict[str, list[ExampleInfo]]:
    """Return examples grouped by category."""
    groups: dict[str, list[ExampleInfo]] = {}
    for info in _REGISTRY.values():
        groups.setdefault(info.category, []).append(info)
    return groups


def get_example(name: str) -> ExampleInfo | None:
    """Look up a single example by name."""
    return _REGISTRY.get(name)


def get_lessons() -> list[Lesson]:
    """Return all lessons in order."""
    return LESSONS


def get_lesson(number: int) -> Lesson | None:
    """Look up a lesson by number."""
    for lesson in LESSONS:
        if lesson.number == number:
            return lesson
    return None


def examples_for_lesson(lesson: Lesson) -> list[ExampleInfo]:
    """Return all examples belonging to a lesson, in registration order."""
    by_cat = get_by_category()
    result: list[ExampleInfo] = []
    for cat in lesson.categories:
        result.extend(by_cat.get(cat, []))
    return result


def examples_in_lesson_order() -> list[ExampleInfo]:
    """Return all examples ordered by lesson progression."""
    seen: set[str] = set()
    result: list[ExampleInfo] = []
    for lesson in LESSONS:
        for info in examples_for_lesson(lesson):
            if info.name not in seen:
                seen.add(info.name)
                result.append(info)
    # Include any examples not assigned to a lesson at the end
    for info in _REGISTRY.values():
        if info.name not in seen:
            result.append(info)
    return result


def show(code: str | Callable[..., Any] | type, result: Any = None) -> None:
    """Print a code snippet (plain, copy-pasteable) and optional result.

    Accepts a string, function, or class.  When given a callable or type,
    the source is extracted automatically via ``inspect.getsource()``.
    """
    if not isinstance(code, str):
        import inspect
        import textwrap

        code = textwrap.dedent(inspect.getsource(code))

    print()
    for line in code.strip().splitlines():
        print(f"    {line}")
    print()
    if result is not None:
        print(result)
