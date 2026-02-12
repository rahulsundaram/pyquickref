"""Modern Python features (3.10+) for PyQuickRef.

This module demonstrates dataclasses, pattern matching, generators,
walrus operator, and enums.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any


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


def dataclass_example(self: Any) -> None:
    """Demonstrate dataclasses with auto-generated methods."""
    self.logger.info("Demonstrating dataclasses")

    # Basic dataclass — __init__, __repr__, __eq__ are auto-generated
    p1 = Point(3.0, 4.0)
    p2 = Point(0.0, 0.0)
    print(f"Point: {p1}")
    print(f"Distance to origin: {p1.distance_to(p2):.1f}")
    print(f"Points equal: {p1 == Point(3.0, 4.0)}")

    # Dataclass with defaults and field factories
    cfg = Config(name="app", tags=["web", "api"])
    print(f"Config: {cfg}")


def pattern_matching(self: Any) -> None:
    """Demonstrate structural pattern matching (match/case)."""
    self.logger.info("Demonstrating pattern matching")

    # Match on value
    def http_status(code: int) -> str:
        match code:
            case 200:
                return "OK"
            case 404:
                return "Not Found"
            case 500:
                return "Internal Server Error"
            case _:
                return f"Unknown ({code})"

    for code in [200, 404, 500, 418]:
        print(f"  HTTP {code}: {http_status(code)}")

    # Match on structure
    def describe(obj: object) -> str:
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


def generator_example(self: Any) -> None:
    """Demonstrate generators and yield."""
    self.logger.info("Demonstrating generators")

    # Generator function with yield
    def fibonacci(n: int) -> Any:
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    print(f"Fibonacci(8): {list(fibonacci(8))}")

    # Generator expression (like list comprehension but lazy)
    squares_gen = (x**2 for x in range(5))
    print(f"Generator expression: {list(squares_gen)}")

    # Walrus operator (:=) in a while loop
    data = [1, 5, 3, 8, 2, 7]
    print("Values > 4 (walrus operator):")
    it = iter(data)
    results = []
    while (val := next(it, None)) is not None:
        if val > 4:
            results.append(val)
    print(f"  {results}")


def enum_example(self: Any) -> None:
    """Demonstrate enums for type-safe constants."""
    self.logger.info("Demonstrating enums")

    print(f"Color.RED: {Color.RED}")
    print(f"Color.RED.value: {Color.RED.value}")
    print(f"All colors: {[c.name for c in Color]}")

    # Enum in match/case
    def describe_color(color: Color) -> str:
        match color:
            case Color.RED:
                return "warm"
            case Color.BLUE:
                return "cool"
            case _:
                return "neutral"

    for color in Color:
        print(f"  {color.name} is {describe_color(color)}")
