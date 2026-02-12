"""Shared test data for examples that operate on data structures."""

from dataclasses import dataclass, field


@dataclass
class SampleData:
    """Fresh sample data for each example invocation — mutations are isolated."""

    testlist: list[str] = field(default_factory=lambda: ["apple", "banana", "cherry"])
    testdict: dict[str, int] = field(default_factory=lambda: {"a": 1, "b": 2, "c": 3})
    testset: set[int] = field(default_factory=lambda: {1, 2, 3})
    testtuple: tuple[int, int, int] = field(default=(10, 20, 30))
    teststring: str = "Python is awesome!"
