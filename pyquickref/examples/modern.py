"""Modern Python features (3.10+) for PyQuickRef.

Dataclasses, pattern matching, generators, walrus operator, enums, type hints.
Docs: https://docs.python.org/3/whatsnew/3.10.html
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any

from pyquickref.registry import example, show


class Color(Enum):
    """Example enum for colors."""

    RED = auto()
    GREEN = auto()
    BLUE = auto()


@dataclass
class Point:
    """A 2D point using dataclass."""

    x: float
    y: float

    def distance_to(self: "Point", other: "Point") -> float:
        """Calculate Euclidean distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass
class Config:
    """Configuration with defaults and field factories."""

    name: str
    debug: bool = False
    tags: list[str] = field(default_factory=list)


@example(
    "Modern Python",
    "Dataclasses with auto-generated __init__, __repr__, __eq__",
    doc_url="https://docs.python.org/3/library/dataclasses.html",
)
def dataclass_example() -> None:
    """Demonstrate dataclasses with auto-generated methods."""
    show(Point)

    p1 = Point(3.0, 4.0)
    p2 = Point(0.0, 0.0)
    print(f"Point: {p1}")
    print(f"Distance to origin: {p1.distance_to(p2):.1f}")
    print(f"Points equal: {p1 == Point(3.0, 4.0)}")

    cfg = Config(name="app", tags=["web", "api"])
    print(f"Config: {cfg}")


@example(
    "Modern Python",
    "Structural pattern matching with match/case (3.10+)",
    doc_url="https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching",
)
def pattern_matching() -> None:
    """Demonstrate structural pattern matching (match/case)."""

    def http_status(code: int) -> str:
        """Map an HTTP status code to its description."""
        match code:
            case 200:
                return "OK"
            case 404:
                return "Not Found"
            case 500:
                return "Internal Server Error"
            case _:
                return f"Unknown ({code})"

    show(http_status)
    for code in [200, 404, 500, 418]:
        print(f"  HTTP {code}: {http_status(code)}")

    def describe(obj: object) -> str:
        """Describe a shape using structural pattern matching."""
        match obj:
            case {"type": "circle", "radius": r}:
                return f"Circle with radius {r}"
            case {"type": "rect", "width": w, "height": h}:
                return f"Rectangle {w}x{h}"
            case [x, y]:
                return f"2D point ({x}, {y})"
            case _:
                return f"Unknown: {obj}"

    shapes: list[object] = [
        {"type": "circle", "radius": 5},
        {"type": "rect", "width": 3, "height": 4},
        [10, 20],
    ]
    for shape in shapes:
        print(f"  {describe(shape)}")


@example(
    "Modern Python",
    "Generator functions, expressions, and walrus operator",
    doc_url="https://docs.python.org/3/howto/functional.html#generators",
)
def generator_example() -> None:
    """Demonstrate generators and yield."""

    def fibonacci(n: int) -> Any:
        """Yield the first n Fibonacci numbers."""
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    show(fibonacci)
    print(f"Fibonacci(8): {list(fibonacci(8))}")

    show("squares_gen = (x**2 for x in range(5))")
    squares_gen = (x**2 for x in range(5))
    print(f"Generator expression: {list(squares_gen)}")

    show(
        "while (val := next(it, None)) is not None:\n"
        "    if val > 4: results.append(val)"
    )
    data = [1, 5, 3, 8, 2, 7]
    print("Values > 4 (walrus operator):")
    it = iter(data)
    results = []
    while (val := next(it, None)) is not None:
        if val > 4:
            results.append(val)
    print(f"  {results}")


@example(
    "Modern Python",
    "Enums for type-safe constants with match/case",
    doc_url="https://docs.python.org/3/library/enum.html",
)
def enum_example() -> None:
    """Demonstrate enums for type-safe constants."""
    show(Color)
    print(f"Color.RED: {Color.RED}")
    print(f"Color.RED.value: {Color.RED.value}")
    print(f"All colors: {[c.name for c in Color]}")

    def describe_color(color: Color) -> str:
        """Return a temperature description for a color."""
        match color:
            case Color.RED:
                return "warm"
            case Color.BLUE:
                return "cool"
            case _:
                return "neutral"

    for color in Color:
        print(f"  {color.name} is {describe_color(color)}")


@example(
    "Modern Python",
    "Walrus operator (:=) in while loops, comprehensions, and if",
    doc_url="https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions",
)
def walrus_operator() -> None:
    """Demonstrate the walrus operator (:=) for inline assignment."""
    show(
        "data = [1, 5, 3, 8, 2, 7]\n"
        "it = iter(data)\n"
        "while (val := next(it, None)) is not None:\n"
        "    if val > 4: big.append(val)"
    )
    data = [1, 5, 3, 8, 2, 7]
    it = iter(data)
    big: list[int] = []
    while (val := next(it, None)) is not None:
        if val > 4:
            big.append(val)
    print(f"Values > 4: {big}")

    show("[y for x in range(10) if (y := x**2) > 20]")
    result = [y for x in range(10) if (y := x**2) > 20]
    print(f"Squares > 20: {result}")

    show("text = 'Hello World'\nif (n := len(text)) > 5:\n    print(f'{n} chars')")
    text = "Hello World"
    if (n := len(text)) > 5:
        print(f"Text has {n} characters (> 5)")


@example(
    "Modern Python",
    "Type hints: basic annotations, Optional, Union, generics",
    doc_url="https://docs.python.org/3/library/typing.html",
)
def type_hints() -> None:
    """Demonstrate type annotations and common typing patterns."""
    show("name: str = 'Python'\nscores: list[int] = [95, 87, 92]")
    name: str = "Python"
    scores: list[int] = [95, 87, 92]
    print(f"name: {name} (annotated as str)")
    print(f"scores: {scores} (annotated as list[int])")

    def find_user(user_id: int) -> str | None:
        """Look up a user by ID, returning None if not found."""
        users = {1: "Alice", 2: "Bob"}
        return users.get(user_id)

    show(find_user)
    print(f"find_user(1) = {find_user(1)!r}")
    print(f"find_user(9) = {find_user(9)!r}")

    show("coords: dict[str, float] = {'lat': 40.7, 'lon': -74.0}")
    coords: dict[str, float] = {"lat": 40.7, "lon": -74.0}
    print(f"coords: {coords} (dict[str, float])")

    from collections.abc import Callable as CallableType

    def apply(func: CallableType[[int], int], val: int) -> int:
        """Apply a function to a value and return the result."""
        return func(val)

    show(apply)
    print(f"apply(lambda x: x*2, 5) = {apply(lambda x: x * 2, 5)}")  # noqa: E731
