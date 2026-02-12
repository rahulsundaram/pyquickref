"""Practical pattern examples for PyQuickRef.

Real-world utility patterns: retry, timeout, pipeline, batching, and more.
"""

import os
import random
import threading
import time
from collections import ChainMap
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from functools import lru_cache, wraps
from itertools import groupby
from typing import Any, NamedTuple

from pyquickref.registry import example, show


@example(
    "Practical Patterns",
    "Retry with exponential backoff and jitter",
    doc_url="https://docs.python.org/3/library/time.html#time.sleep",
)
def retry_backoff() -> None:
    """Demonstrate retry with exponential backoff."""

    def retry(
        func: Callable[..., Any],
        max_attempts: int = 3,
        base_delay: float = 0.01,
    ) -> Any:
        for attempt in range(1, max_attempts + 1):
            try:
                return func()
            except Exception as e:
                if attempt == max_attempts:
                    raise
                delay = base_delay * (2 ** (attempt - 1))
                jitter = random.uniform(0, delay * 0.1)
                time.sleep(delay + jitter)
                print(f"  Attempt {attempt} failed: {e}, retrying...")
        return None

    show(
        "def retry(func, max_attempts=3, base_delay=0.01):\n"
        "    for attempt in range(1, max_attempts + 1):\n"
        "        try:\n"
        "            return func()\n"
        "        except Exception as e:\n"
        "            if attempt == max_attempts: raise\n"
        "            delay = base_delay * (2 ** (attempt - 1))\n"
        "            time.sleep(delay + random.uniform(0, delay * 0.1))"
    )

    call_count = 0

    def flaky_operation() -> str:
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            msg = "connection timeout"
            raise ConnectionError(msg)
        return "success"

    result = retry(flaky_operation, max_attempts=5, base_delay=0.01)
    print(f"  Result: {result} (after {call_count} attempts)")


@example(
    "Practical Patterns",
    "Run a function with a time limit using threading",
    doc_url="https://docs.python.org/3/library/threading.html#timer-objects",
)
def timeout_wrapper() -> None:
    """Demonstrate timeout wrapper using threading."""

    class OperationTimeoutError(Exception):
        pass

    def run_with_timeout(func: Callable[..., Any], seconds: float) -> Any:
        result: list[Any] = []
        exception: list[Exception] = []

        def target() -> None:
            try:
                result.append(func())
            except Exception as e:
                exception.append(e)

        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout=seconds)
        if thread.is_alive():
            raise OperationTimeoutError(f"Timed out after {seconds}s")
        if exception:
            raise exception[0]
        return result[0] if result else None

    show(
        "def run_with_timeout(func, seconds):\n"
        "    thread = threading.Thread(target=...)\n"
        "    thread.start()\n"
        "    thread.join(timeout=seconds)\n"
        "    if thread.is_alive():\n"
        '        raise OperationTimeoutError("Timed out")'
    )

    print(f"  Fast: {run_with_timeout(lambda: 'fast result', seconds=0.5)}")
    try:
        run_with_timeout(lambda: time.sleep(1) or "never", seconds=0.05)
    except OperationTimeoutError as e:
        print(f"  Slow: {e}")


@example(
    "Practical Patterns",
    "Compose functions into a data processing pipeline",
    doc_url="https://docs.python.org/3/library/functools.html#functools.reduce",
)
def pipeline_pattern() -> None:
    """Demonstrate function composition pipeline."""
    from functools import reduce

    def pipeline(*steps: Callable[..., Any]) -> Callable[..., Any]:
        def run(data: Any) -> Any:
            return reduce(lambda d, step: step(d), steps, data)

        return run

    show(
        "def pipeline(*steps):\n"
        "    def run(data):\n"
        "        return reduce(lambda d, step: step(d), steps, data)\n"
        "    return run\n\n"
        "process = pipeline(str.strip, str.lower, str.title)"
    )

    process_name = pipeline(str.strip, str.lower, str.title)
    print(f"  '  JOHN DOE  ' → {process_name('  JOHN DOE  ')!r}")

    process_numbers = pipeline(
        lambda nums: [x for x in nums if x > 0],
        lambda nums: [x**2 for x in nums],
        sum,
    )
    result = process_numbers([-1, 2, -3, 4, 5])
    print(f"  [-1, 2, -3, 4, 5] → filter → square → sum = {result}")


@example(
    "Practical Patterns",
    "Process items in fixed-size chunks for efficient batching",
    doc_url="https://docs.python.org/3/library/itertools.html",
)
def batch_processing() -> None:
    """Demonstrate batch processing with chunked iteration."""

    def batched(iterable: Any, n: int) -> Iterator[list[Any]]:
        from itertools import islice

        it = iter(iterable)
        while batch := list(islice(it, n)):
            yield batch

    show(
        "def batched(iterable, n):\n"
        "    it = iter(iterable)\n"
        "    while batch := list(islice(it, n)):\n"
        "        yield batch"
    )

    items = list(range(1, 11))
    print(f"  Items: {items}")
    print("  Batches of 3:")
    for i, batch in enumerate(batched(items, 3), 1):
        total = sum(batch)
        print(f"    Batch {i}: {batch} → sum={total}")


@example(
    "Practical Patterns",
    "Group records by key and aggregate with itertools.groupby",
    doc_url="https://docs.python.org/3/library/itertools.html#itertools.groupby",
)
def groupby_aggregate() -> None:
    """Demonstrate groupby for grouping and aggregation."""
    sales = [
        {"region": "North", "amount": 100},
        {"region": "South", "amount": 200},
        {"region": "North", "amount": 150},
        {"region": "South", "amount": 300},
        {"region": "North", "amount": 250},
    ]

    show(
        "from itertools import groupby\n\n"
        "sales = [{'region': 'North', 'amount': 100}, ...]\n"
        "sorted_sales = sorted(sales, key=lambda s: s['region'])\n"
        "for region, group in groupby(sorted_sales, key=...):\n"
        "    items = list(group)\n"
        "    total = sum(s['amount'] for s in items)"
    )

    sorted_sales = sorted(sales, key=lambda s: s["region"])
    for region, group in groupby(sorted_sales, key=lambda s: s["region"]):
        items = list(group)
        total = sum(s["amount"] for s in items)
        print(f"  {region}: {len(items)} sales, total=${total}")


@example(
    "Practical Patterns",
    "Merge config sources with ChainMap: defaults → env → overrides",
    doc_url="https://docs.python.org/3/library/collections.html#collections.ChainMap",
)
def config_cascade() -> None:
    """Demonstrate cascading config with ChainMap."""
    defaults = {
        "host": "localhost",
        "port": 8080,
        "debug": False,
        "workers": 4,
    }
    env_config: dict[str, Any] = {}
    if os.environ.get("APP_PORT"):
        env_config["port"] = int(os.environ["APP_PORT"])
    cli_overrides = {"debug": True, "workers": 2}

    show(
        "from collections import ChainMap\n\n"
        "defaults = {'host': 'localhost', 'port': 8080, 'debug': False}\n"
        "env_config = {'port': int(os.environ['APP_PORT'])}  # from env\n"
        "cli_overrides = {'debug': True}\n\n"
        "config = ChainMap(cli_overrides, env_config, defaults)"
    )

    config = ChainMap(cli_overrides, env_config, defaults)
    print(f"  host:    {config['host']}  (from defaults)")
    port_src = "env" if "port" in env_config else "defaults"
    print(f"  port:    {config['port']}  (from {port_src})")
    print(f"  debug:   {config['debug']}  (from cli override)")
    print(f"  workers: {config['workers']}  (from cli override)")
    print(f"  Layers: {list(config.maps)}")


@example(
    "Practical Patterns",
    "Early returns to avoid deep nesting — flat is better than nested",
    doc_url="https://docs.python.org/3/glossary.html#term-EAFP",
)
def guard_clauses() -> None:
    """Demonstrate guard clause pattern vs deep nesting."""
    show(
        "# Bad: deeply nested\n"
        "def process(user):\n"
        "    if user:\n"
        "        if user.active:\n"
        "            if user.verified:\n"
        "                return do_work(user)\n\n"
        "# Good: guard clauses\n"
        "def process(user):\n"
        "    if not user: return None\n"
        "    if not user.active: return 'inactive'\n"
        "    if not user.verified: return 'unverified'\n"
        "    return do_work(user)"
    )

    @dataclass
    class User:
        name: str
        active: bool = True
        verified: bool = True
        age: int = 25

    def validate_user(user: User | None) -> str:
        if user is None:
            return "error: no user"
        if not user.active:
            return f"error: {user.name} is inactive"
        if not user.verified:
            return f"error: {user.name} is unverified"
        if user.age < 18:
            return f"error: {user.name} is underage"
        return f"ok: {user.name} is valid"

    cases: list[User | None] = [
        None,
        User("Alice", active=False),
        User("Bob", verified=False),
        User("Charlie", age=15),
        User("Diana"),
    ]
    for case in cases:
        print(f"  {validate_user(case)}")


@example(
    "Practical Patterns",
    "Frozen dataclasses and NamedTuple for safe value objects",
    doc_url="https://docs.python.org/3/library/dataclasses.html#frozen-instances",
)
def immutable_data() -> None:
    """Demonstrate immutable data patterns."""

    @dataclass(frozen=True)
    class Point:
        x: float
        y: float

    class Color(NamedTuple):
        r: int
        g: int
        b: int

    show(
        "@dataclass(frozen=True)\n"
        "class Point:\n"
        "    x: float\n"
        "    y: float\n\n"
        "class Color(NamedTuple):\n"
        "    r: int\n"
        "    g: int\n"
        "    b: int"
    )

    p = Point(3.0, 4.0)
    print(f"  Point: {p}")
    try:
        p.x = 5.0  # type: ignore[misc]
    except AttributeError:
        print("  p.x = 5.0 → AttributeError (frozen!)")

    c = Color(255, 128, 0)
    print(f"  Color: {c}")
    print(f"  As dict: {c._asdict()}")
    print(f"  Hashable — can use as dict key: {hash(p)!r}")
    print(f"  Equal by value: {Point(3.0, 4.0) == p}")


@example(
    "Practical Patterns",
    "Manual memoization vs functools.lru_cache for caching results",
    doc_url="https://docs.python.org/3/library/functools.html#functools.lru_cache",
)
def memoize_pattern() -> None:
    """Demonstrate memoization patterns."""
    show(
        "# Manual memoization\n"
        "def memoize(func):\n"
        "    cache = {}\n"
        "    def wrapper(*args):\n"
        "        if args not in cache:\n"
        "            cache[args] = func(*args)\n"
        "        return cache[args]\n"
        "    return wrapper\n\n"
        "# Or use lru_cache\n"
        "@lru_cache(maxsize=128)\n"
        "def fibonacci(n): ..."
    )

    call_count = 0

    @lru_cache(maxsize=128)
    def fib(n: int) -> int:
        nonlocal call_count
        call_count += 1
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    result = fib(30)
    print(f"  fib(30) = {result}")
    print(f"  Function calls: {call_count} (not 2^30!)")
    info = fib.cache_info()
    print(f"  Cache: hits={info.hits}, misses={info.misses}, size={info.currsize}")

    def memoize(
        func: Callable[..., Any],
    ) -> Callable[..., Any]:
        cache: dict[Any, Any] = {}

        @wraps(func)
        def wrapper(*args: Any) -> Any:
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]

        wrapper.cache = cache  # type: ignore[attr-defined]
        return wrapper

    @memoize
    def expensive(n: int) -> int:
        return n * n

    expensive(5)
    expensive(5)
    expensive(10)
    print(f"  Manual cache: {expensive.cache}")  # type: ignore[attr-defined]
