"""Standard library tools examples for PyQuickRef.

pathlib, datetime/zoneinfo, functools, and asyncio.
"""

import asyncio
import tempfile
from datetime import datetime, timedelta, timezone
from functools import lru_cache, partial, reduce
from pathlib import Path

from pyquickref.registry import example, show


@example(
    "Stdlib Tools",
    "Path operations: parent, name, suffix, glob, read/write",
    doc_url="https://docs.python.org/3/library/pathlib.html",
)
def pathlib_example() -> None:
    """Demonstrate pathlib.Path operations."""
    p = Path("/usr/local/bin/python3")
    show("p = Path('/usr/local/bin/python3')")
    print(f"parent : {p.parent}")
    print(f"name   : {p.name}")
    print(f"stem   : {p.stem}")
    print(f"suffix : {p.suffix}")
    print(f"parts  : {p.parts}")

    # Glob in a temp directory
    show("Path(tmp).glob('*.txt')")
    with tempfile.TemporaryDirectory() as tmp:
        for name in ["a.txt", "b.txt", "c.py"]:
            Path(tmp, name).write_text(f"content of {name}")
        txt_files = sorted(p.name for p in Path(tmp).glob("*.txt"))
        print(f"glob('*.txt'): {txt_files}")


@example(
    "Stdlib Tools",
    "Timezone-aware datetimes with zoneinfo, timedelta, ISO format",
    doc_url="https://docs.python.org/3/library/datetime.html",
)
def datetime_example() -> None:
    """Demonstrate timezone-aware datetimes."""
    now = datetime.now(tz=timezone.utc)
    show(
        "from datetime import datetime, timedelta, timezone\n"
        "now = datetime.now(tz=timezone.utc)"
    )
    print(f"UTC now     : {now.isoformat()}")

    tomorrow = now + timedelta(days=1)
    show("tomorrow = now + timedelta(days=1)")
    print(f"Tomorrow    : {tomorrow.isoformat()}")

    show("now.strftime('%Y-%m-%d %H:%M')")
    print(f"Formatted   : {now.strftime('%Y-%m-%d %H:%M')}")

    # Parsing
    show("datetime.fromisoformat('2024-01-15T10:30:00+00:00')")
    parsed = datetime.fromisoformat("2024-01-15T10:30:00+00:00")
    print(f"Parsed      : {parsed}")


@example(
    "Stdlib Tools",
    "lru_cache, partial, reduce from functools",
    doc_url="https://docs.python.org/3/library/functools.html",
)
def functools_example() -> None:
    """Demonstrate functools utilities."""
    # lru_cache
    show(
        "@lru_cache(maxsize=128)\n"
        "def fib(n):\n"
        "    return n if n < 2 else fib(n-1) + fib(n-2)"
    )

    @lru_cache(maxsize=128)
    def fib(n: int) -> int:
        return n if n < 2 else fib(n - 1) + fib(n - 2)

    print(f"fib(10) = {fib(10)}")
    print(f"cache_info: {fib.cache_info()}")

    # partial
    show("double = partial(mul, 2)")

    def mul(a: int, b: int) -> int:
        return a * b

    double = partial(mul, 2)
    print(f"double(5) = {double(5)}")

    # reduce
    show("reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])")
    total = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
    print(f"reduce sum = {total}")


@example(
    "Stdlib Tools",
    "async/await, gather, concurrent tasks with asyncio",
    doc_url="https://docs.python.org/3/library/asyncio.html",
)
def asyncio_example() -> None:
    """Demonstrate async/await and asyncio.gather."""

    async def fetch(name: str, delay: float) -> str:
        await asyncio.sleep(delay)
        return f"{name} done ({delay}s)"

    async def main() -> None:
        show(
            "async def fetch(name, delay):\n"
            "    await asyncio.sleep(delay)\n"
            "    return f'{name} done'"
        )
        # Sequential
        show("result = await fetch('A', 0.1)")
        result = await fetch("A", 0.1)
        print(f"Sequential: {result}")

        # Concurrent with gather
        show("results = await asyncio.gather(fetch('B', 0.1), fetch('C', 0.1))")
        results = await asyncio.gather(
            fetch("B", 0.1),
            fetch("C", 0.1),
            fetch("D", 0.1),
        )
        for r in results:
            print(f"Gathered: {r}")

    asyncio.run(main())
