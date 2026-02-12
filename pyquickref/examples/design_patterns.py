"""Design pattern examples for PyQuickRef.

Factory, strategy, observer, builder, producer/consumer, and rate limiter.
Docs: https://refactoring.guru/design-patterns/python
"""

import queue
import threading
import time
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


@example(
    "Design Patterns",
    "Step-by-step object construction with a fluent builder API",
    doc_url="https://refactoring.guru/design-patterns/builder/python",
)
def builder_pattern() -> None:
    """Demonstrate the builder pattern with fluent interface."""

    @dataclass
    class HttpRequest:
        method: str = "GET"
        url: str = ""
        headers: dict[str, str] = field(default_factory=dict)
        body: str = ""
        timeout: float = 30.0

    class RequestBuilder:
        def __init__(self: "RequestBuilder") -> None:
            self._request = HttpRequest()

        def method(self: "RequestBuilder", method: str) -> "RequestBuilder":
            self._request.method = method
            return self

        def url(self: "RequestBuilder", url: str) -> "RequestBuilder":
            self._request.url = url
            return self

        def header(self: "RequestBuilder", key: str, value: str) -> "RequestBuilder":
            self._request.headers[key] = value
            return self

        def body(self: "RequestBuilder", body: str) -> "RequestBuilder":
            self._request.body = body
            return self

        def timeout(self: "RequestBuilder", seconds: float) -> "RequestBuilder":
            self._request.timeout = seconds
            return self

        def build(self: "RequestBuilder") -> HttpRequest:
            if not self._request.url:
                msg = "URL is required"
                raise ValueError(msg)
            return self._request

    show(
        "request = (RequestBuilder()\n"
        "    .method('POST')\n"
        "    .url('https://api.example.com/users')\n"
        "    .header('Content-Type', 'application/json')\n"
        '    .body(\'{"name": "Alice"}\')\n'
        "    .timeout(10.0)\n"
        "    .build())"
    )

    req = (
        RequestBuilder()
        .method("POST")
        .url("https://api.example.com/users")
        .header("Content-Type", "application/json")
        .header("Authorization", "Bearer token123")
        .body('{"name": "Alice"}')
        .timeout(10.0)
        .build()
    )
    print(f"  {req.method} {req.url}")
    print(f"  Headers: {req.headers}")
    print(f"  Body: {req.body}")
    print(f"  Timeout: {req.timeout}s")


@example(
    "Design Patterns",
    "Producer/consumer with queue.Queue for decoupled processing",
    doc_url="https://docs.python.org/3/library/queue.html",
)
def producer_consumer() -> None:
    """Demonstrate producer/consumer with threading and Queue."""
    show(
        "q = queue.Queue(maxsize=5)\n\n"
        "def producer(q, items):\n"
        "    for item in items:\n"
        "        q.put(item)\n"
        "    q.put(None)  # sentinel\n\n"
        "def consumer(q):\n"
        "    while (item := q.get()) is not None:\n"
        "        process(item)"
    )

    results: list[str] = []
    q: queue.Queue[int | None] = queue.Queue(maxsize=3)

    def producer(items: list[int]) -> None:
        for item in items:
            q.put(item)
        q.put(None)

    def consumer() -> None:
        while (item := q.get()) is not None:
            results.append(f"{item}→{item**2}")
            q.task_done()
        q.task_done()

    items = [1, 2, 3, 4, 5]
    prod = threading.Thread(target=producer, args=(items,))
    cons = threading.Thread(target=consumer)

    prod.start()
    cons.start()
    prod.join()
    cons.join()

    print(f"  Produced: {items}")
    print(f"  Consumed: [{', '.join(results)}]")
    print(f"  Queue empty: {q.empty()}")


@example(
    "Design Patterns",
    "Token bucket rate limiter for controlling throughput",
    doc_url="https://docs.python.org/3/library/time.html#time.monotonic",
)
def rate_limiter() -> None:
    """Demonstrate token bucket rate limiter."""

    class TokenBucket:
        def __init__(self: "TokenBucket", rate: float, capacity: int) -> None:
            self.rate = rate
            self.capacity = capacity
            self.tokens = float(capacity)
            self.last_refill = time.monotonic()

        def _refill(self: "TokenBucket") -> None:
            now = time.monotonic()
            elapsed = now - self.last_refill
            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
            self.last_refill = now

        def acquire(self: "TokenBucket") -> bool:
            self._refill()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False

    show(
        "class TokenBucket:\n"
        "    def __init__(self, rate, capacity):\n"
        "        self.rate = rate       # tokens per second\n"
        "        self.capacity = capacity\n\n"
        "    def acquire(self) -> bool:\n"
        "        self._refill()\n"
        "        if self.tokens >= 1:\n"
        "            self.tokens -= 1\n"
        "            return True\n"
        "        return False"
    )

    bucket = TokenBucket(rate=5, capacity=3)
    print(f"  Rate: {bucket.rate}/s, capacity: {bucket.capacity}")

    allowed = 0
    denied = 0
    for i in range(6):
        if bucket.acquire():
            allowed += 1
            print(f"  Request {i + 1}: allowed")
        else:
            denied += 1
            print(f"  Request {i + 1}: denied (rate limited)")

    print(f"  Total: {allowed} allowed, {denied} denied")
