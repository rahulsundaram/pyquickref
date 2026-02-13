"""Advanced type system examples for PyQuickRef.

Generics, TypeVar, overload, TypeAlias, ParamSpec.
Docs: https://docs.python.org/3/library/typing.html
"""

from collections.abc import Callable
from typing import Generic, TypeVar, overload

from pyquickref.registry import example, show


@example(
    "Type System",
    "Generics: TypeVar, Generic[T], bounded types, constrained types",
    doc_url="https://docs.python.org/3/library/typing.html#generics",
)
def generics_example() -> None:
    """Demonstrate generic types with TypeVar and Generic."""
    # Basic TypeVar
    T = TypeVar("T")

    def first(items: list[T]) -> T:
        """Return the first item, preserving the type."""
        return items[0]

    show("T = TypeVar('T')\ndef first(items: list[T]) -> T:\n    return items[0]")
    print(f"first([1, 2, 3])     = {first([1, 2, 3])}")
    print(f"first(['a', 'b'])    = {first(['a', 'b'])}")

    # Generic class
    V = TypeVar("V")

    class Stack(Generic[V]):
        """A typed stack."""

        def __init__(self) -> None:
            self._items: list[V] = []

        def push(self, item: V) -> None:
            self._items.append(item)

        def pop(self) -> V:
            return self._items.pop()

        def __repr__(self) -> str:
            return f"Stack({self._items})"

    show(Stack)
    s: Stack[int] = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Stack after pushes: {s}")
    print(f"pop() = {s.pop()}")
    print(f"Stack after pop: {s}")

    # Bounded TypeVar — constrained to types with specific capabilities
    Comparable = TypeVar("Comparable", int, float, str)

    def clamp(value: Comparable, lo: Comparable, hi: Comparable) -> Comparable:
        """Clamp a value between lo and hi."""
        return max(lo, min(hi, value))

    show(
        "Comparable = TypeVar('Comparable', int, float, str)\n"
        "def clamp(value: Comparable, lo: Comparable, hi: Comparable) -> Comparable:"
    )
    print(f"clamp(15, 0, 10)       = {clamp(15, 0, 10)}")
    print(f"clamp(3.5, 1.0, 5.0)  = {clamp(3.5, 1.0, 5.0)}")
    print(f"clamp('m', 'a', 'z')  = {clamp('m', 'a', 'z')}")


@example(
    "Type System",
    "overload, TypeAlias, ParamSpec for advanced annotations",
    doc_url="https://docs.python.org/3/library/typing.html#typing.overload",
)
def advanced_typing() -> None:
    """Demonstrate overload, TypeAlias, and ParamSpec."""
    from typing import ParamSpec, TypeAlias

    # TypeAlias — readable names for complex types
    show("UserId: TypeAlias = int\nUserMap: TypeAlias = dict[UserId, str]")
    UserId: TypeAlias = int
    UserMap: TypeAlias = dict[UserId, str]
    users: UserMap = {1: "Alice", 2: "Bob"}
    print(f"users: {users}")
    print(f"UserMap is dict[int, str]: {UserMap}")

    # @overload — different return types based on input
    @overload
    def process(data: str) -> list[str]: ...
    @overload
    def process(data: list[str]) -> str: ...

    def process(data: str | list[str]) -> list[str] | str:
        """Split strings, join lists."""
        if isinstance(data, str):
            return data.split()
        return " ".join(data)

    show(
        "@overload\n"
        "def process(data: str) -> list[str]: ...\n"
        "@overload\n"
        "def process(data: list[str]) -> str: ...\n\n"
        "def process(data: str | list[str]) -> list[str] | str:\n"
        "    if isinstance(data, str): return data.split()\n"
        "    return ' '.join(data)"
    )
    print(f"process('hello world')     = {process('hello world')}")
    print(f"process(['hello', 'world']) = {process(['hello', 'world'])}")

    # ParamSpec — preserve function signatures in decorators
    P = ParamSpec("P")  # noqa: N806
    R = TypeVar("R")

    import functools

    def logged(func: Callable[P, R]) -> Callable[P, R]:
        """Log calls while preserving type info."""

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            name = getattr(func, "__name__", repr(func))
            print(f"  Calling {name}")
            return func(*args, **kwargs)

        return wrapper

    show(
        "P = ParamSpec('P')\nR = TypeVar('R')\n"
        "def logged(func: Callable[P, R]) -> Callable[P, R]:"
    )

    @logged
    def add(a: int, b: int) -> int:
        return a + b

    result = add(3, 4)
    print(f"  Result: {result}")
