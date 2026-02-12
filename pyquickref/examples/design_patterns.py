"""Design pattern examples for PyQuickRef.

Factory, strategy, and observer patterns in Python.
Docs: https://refactoring.guru/design-patterns/python
"""

from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass, field

from pyquickref.registry import example, show


@example(
    "Design Patterns",
    "ABC + factory function to create objects by type",
    doc_url="https://docs.python.org/3/library/abc.html",
)
def factory_pattern() -> None:
    """Demonstrate the factory pattern using ABC and a factory function."""

    class Notification(ABC):
        @abstractmethod
        def send(self: "Notification", message: str) -> str: ...

    class EmailNotification(Notification):
        def send(self: "EmailNotification", message: str) -> str:
            return f"Email: {message}"

    class SMSNotification(Notification):
        def send(self: "SMSNotification", message: str) -> str:
            return f"SMS: {message}"

    class PushNotification(Notification):
        def send(self: "PushNotification", message: str) -> str:
            return f"Push: {message}"

    types: dict[str, type[Notification]] = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
    }

    def create_notification(kind: str) -> Notification:
        cls = types.get(kind)
        if cls is None:
            msg = f"Unknown notification type: {kind}"
            raise ValueError(msg)
        return cls()

    show("def create_notification(kind: str):\n    return types[kind]()")
    for kind in ["email", "sms", "push"]:
        notif = create_notification(kind)
        print(f"  {notif.send('Hello!')}")


@example(
    "Design Patterns",
    "Callables as interchangeable strategies on a dataclass",
    doc_url="https://docs.python.org/3/library/dataclasses.html",
)
def strategy_pattern() -> None:
    """Demonstrate the strategy pattern with callable strategies."""

    def full_price(amount: float) -> float:
        return amount

    def ten_percent_off(amount: float) -> float:
        return amount * 0.9

    def member_discount(amount: float) -> float:
        return amount * 0.8

    @dataclass
    class Order:
        total: float
        pricing: Callable[[float], float] = full_price

        def final_price(self: "Order") -> float:
            return self.pricing(self.total)

    show(
        "@dataclass\nclass Order:\n    total: float\n"
        "    pricing: Callable[[float], float] = full_price\n\n"
        "    def final_price(self):\n"
        "        return self.pricing(self.total)"
    )
    strategies = [
        ("full_price", full_price),
        ("ten_percent_off", ten_percent_off),
        ("member_discount", member_discount),
    ]
    for name, strategy in strategies:
        order = Order(total=100.0, pricing=strategy)
        print(f"  {name}: ${order.final_price():.2f}")


@example(
    "Design Patterns",
    "EventEmitter with .on() / .emit() for pub/sub",
    doc_url="https://docs.python.org/3/library/asyncio-eventloop.html",
)
def observer_pattern() -> None:
    """Demonstrate the observer pattern with an event emitter."""

    @dataclass
    class EventEmitter:
        _listeners: dict[str, list[Callable[..., None]]] = field(default_factory=dict)

        def on(self: "EventEmitter", event: str, callback: Callable[..., None]) -> None:
            self._listeners.setdefault(event, []).append(callback)

        def emit(self: "EventEmitter", event: str, *args: object) -> None:
            for cb in self._listeners.get(event, []):
                cb(*args)

    show(
        "emitter = EventEmitter()\n"
        "emitter.on('login', lambda user: print(f'Welcome {user}'))\n"
        "emitter.emit('login', 'Alice')"
    )
    emitter = EventEmitter()
    emitter.on("login", lambda user: print(f"  Welcome, {user}!"))
    emitter.on("login", lambda user: print(f"  Audit: {user} logged in"))
    emitter.on("logout", lambda user: print(f"  Goodbye, {user}!"))

    emitter.emit("login", "Alice")
    emitter.emit("logout", "Alice")
