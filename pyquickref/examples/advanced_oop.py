"""Advanced OOP examples for PyQuickRef.

Descriptors, metaclasses, protocols, and abstract base classes.
Docs: https://docs.python.org/3/reference/datamodel.html#descriptors
"""

from abc import ABC, abstractmethod
from typing import Any, Protocol, runtime_checkable

from pyquickref.registry import example, show


@example(
    "Advanced OOP",
    "Descriptors: __get__/__set__/__delete__, how @property works",
    doc_url="https://docs.python.org/3/howto/descriptor.html",
)
def descriptors_example() -> None:
    """Demonstrate descriptors — the mechanism behind @property."""

    class Validated:
        """A descriptor that validates values are positive."""

        def __init__(self, name: str) -> None:
            self.name = name
            self.storage_name = f"_validated_{name}"

        def __get__(self, obj: Any, objtype: type | None = None) -> Any:
            if obj is None:
                return self
            return getattr(obj, self.storage_name, None)

        def __set__(self, obj: Any, value: Any) -> None:
            if not isinstance(value, int | float) or value < 0:
                msg = f"{self.name} must be non-negative, got {value!r}"
                raise ValueError(msg)
            setattr(obj, self.storage_name, value)

        def __delete__(self, obj: Any) -> None:
            delattr(obj, self.storage_name)

    show(Validated)

    class Product:
        """A product with validated price and quantity."""

        price = Validated("price")
        quantity = Validated("quantity")

        def __init__(self, name: str, price: float, quantity: int) -> None:
            self.name = name
            self.price = price  # Goes through Validated.__set__
            self.quantity = quantity

    show(Product)
    p = Product("Widget", 9.99, 5)
    print(f"Product: {p.name}, price={p.price}, qty={p.quantity}")

    # Validation in action
    show("p.price = -1  # raises ValueError")
    try:
        p.price = -1
    except ValueError as e:
        print(f"Caught: {e}")

    # How @property is actually a descriptor
    show(
        "# @property is a descriptor with __get__, __set__, __delete__\n"
        "# property(fget, fset, fdel, doc)"
    )
    print(f"property has __get__: {hasattr(property, '__get__')}")
    print(f"property has __set__: {hasattr(property, '__set__')}")


@example(
    "Advanced OOP",
    "Metaclasses: type(), __new__, __init_subclass__",
    doc_url="https://docs.python.org/3/reference/datamodel.html#metaclasses",
)
def metaclass_example() -> None:
    """Demonstrate metaclasses and class creation hooks."""
    # type() creates classes dynamically
    show("MyClass = type('MyClass', (object,), {'x': 10, 'greet': lambda self: 'hi'})")
    my_cls = type("MyClass", (object,), {"x": 10, "greet": lambda self: "hi"})  # noqa: N806
    obj = my_cls()
    print(f"type(MyClass) = {type(my_cls).__name__}")
    print(f"obj.x = {obj.x}, obj.greet() = {obj.greet()}")  # type: ignore[attr-defined]

    # Custom metaclass
    class RegistryMeta(type):
        """A metaclass that auto-registers all subclasses."""

        _registry: dict[str, type] = {}

        def __new__(mcs, name: str, bases: tuple, namespace: dict) -> type:  # noqa: ANN001
            cls = super().__new__(mcs, name, bases, namespace)
            if bases:  # Don't register the base class itself
                mcs._registry[name] = cls
            return cls

    show(RegistryMeta)

    class Plugin(metaclass=RegistryMeta):
        """Base class for auto-registered plugins."""

    class AuthPlugin(Plugin):
        pass

    class CachePlugin(Plugin):
        pass

    print(f"Registered: {list(RegistryMeta._registry.keys())}")

    # __init_subclass__ — simpler alternative to metaclasses (3.6+)
    class Base:
        _subclasses: list[str] = []

        def __init_subclass__(cls, **kwargs: Any) -> None:
            super().__init_subclass__(**kwargs)
            Base._subclasses.append(cls.__name__)

    show(Base)

    class Foo(Base):
        pass

    class Bar(Base):
        pass

    print(f"__init_subclass__ tracked: {Base._subclasses}")


@example(
    "Advanced OOP",
    "Protocols (structural subtyping) and ABCs (nominal subtyping)",
    doc_url="https://docs.python.org/3/library/typing.html#typing.Protocol",
)
def protocols_abcs() -> None:
    """Demonstrate Protocols vs ABCs for defining interfaces."""

    # Protocol — structural subtyping (duck typing with type safety)
    @runtime_checkable
    class Drawable(Protocol):
        def draw(self) -> str: ...

    show(Drawable)

    class Circle:
        def draw(self) -> str:
            return "Drawing circle"

    class Square:
        def draw(self) -> str:
            return "Drawing square"

    # No inheritance needed — just implement the method
    c = Circle()
    print(f"isinstance(Circle(), Drawable) = {isinstance(c, Drawable)}")
    print(f"Circle().draw() = {c.draw()}")

    # ABC — nominal subtyping (must explicitly inherit)
    class Serializable(ABC):
        @abstractmethod
        def serialize(self) -> str:
            """Convert to string representation."""

        @abstractmethod
        def deserialize(self, data: str) -> None:
            """Load from string representation."""

    show(Serializable)

    class JsonRecord(Serializable):
        def __init__(self, data: dict[str, Any] | None = None) -> None:
            self.data = data or {}

        def serialize(self) -> str:
            import json

            return json.dumps(self.data)

        def deserialize(self, data: str) -> None:
            import json

            self.data = json.loads(data)

    show(JsonRecord)
    record = JsonRecord({"name": "Alice"})
    print(f"serialize: {record.serialize()}")
    is_ser = isinstance(record, Serializable)
    print(f"isinstance(JsonRecord(), Serializable) = {is_ser}")

    # Can't instantiate ABC directly
    show("Serializable()  # raises TypeError")
    try:
        Serializable()
    except TypeError as e:
        print(f"Caught: {e}")
