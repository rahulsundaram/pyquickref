"""Concurrency examples for PyQuickRef.

asyncio, threading, multiprocessing, and the GIL.
Docs: https://docs.python.org/3/library/concurrency.html
"""

import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor

from pyquickref.registry import example, show


def _cube(n: int) -> int:
    """CPU-bound work (module-level so it can be pickled for multiprocessing)."""
    return n**3


@example(
    "Concurrency",
    "async/await, gather, concurrent tasks with asyncio",
    doc_url="https://docs.python.org/3/library/asyncio.html",
)
def asyncio_example() -> None:
    """Demonstrate async/await and asyncio.gather."""

    async def fetch(name: str, delay: float) -> str:
        """Simulate an async network request."""
        await asyncio.sleep(delay)
        return f"{name} done ({delay}s)"

    async def main() -> None:
        """Run sequential and concurrent async tasks."""
        show(fetch)
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


@example(
    "Concurrency",
    "Threading: Thread, Lock, ThreadPoolExecutor",
    doc_url="https://docs.python.org/3/library/threading.html",
)
def threading_example() -> None:
    """Demonstrate threading with locks and thread pools."""
    # Basic thread
    results: list[str] = []

    def worker(name: str) -> None:
        results.append(f"{name} done")

    show("t = threading.Thread(target=worker, args=('task-1',))\nt.start()\nt.join()")
    t = threading.Thread(target=worker, args=("task-1",))
    t.start()
    t.join()
    print(f"Thread result: {results}")

    # Lock for thread safety
    counter = {"value": 0}
    lock = threading.Lock()

    def increment(n: int) -> None:
        for _ in range(n):
            with lock:
                counter["value"] += 1

    show("lock = threading.Lock()\nwith lock:\n    counter += 1")
    threads = [threading.Thread(target=increment, args=(1000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Counter after 4 threads x 1000: {counter['value']}")

    # ThreadPoolExecutor — simpler API
    def square(n: int) -> int:
        return n * n

    show(
        "with ThreadPoolExecutor(max_workers=3) as pool:\n"
        "    results = list(pool.map(square, range(5)))"
    )
    with ThreadPoolExecutor(max_workers=3) as pool:
        squares = list(pool.map(square, range(5)))
    print(f"ThreadPool squares: {squares}")


@example(
    "Concurrency",
    "Multiprocessing: Process, Pool, GIL explanation",
    doc_url="https://docs.python.org/3/library/multiprocessing.html",
)
def multiprocessing_example() -> None:
    """Demonstrate multiprocessing and explain the GIL."""
    # GIL explanation (shown as documentation, not runnable)
    show(
        "# The GIL (Global Interpreter Lock)\n"
        "# - CPython allows only one thread to execute Python bytecode at a time\n"
        "# - Threading is good for I/O-bound tasks (waiting on network, disk)\n"
        "# - Multiprocessing bypasses GIL — each process has its own interpreter\n"
        "# - Use multiprocessing for CPU-bound tasks (math, data processing)"
    )
    print("GIL: threads share memory, processes have separate memory")
    print("  I/O-bound  -> use threading or asyncio")
    print("  CPU-bound  -> use multiprocessing")

    # ProcessPoolExecutor (uses separate processes)
    from concurrent.futures import ProcessPoolExecutor

    show(
        "def cube(n: int) -> int:\n"
        "    return n ** 3\n\n"
        "with ProcessPoolExecutor(max_workers=2) as pool:\n"
        "    results = list(pool.map(cube, range(5)))"
    )
    with ProcessPoolExecutor(max_workers=2) as pool:
        cubes = list(pool.map(_cube, range(5)))
    print(f"ProcessPool cubes: {cubes}")

    # multiprocessing.Value for shared state
    import multiprocessing

    show("shared = multiprocessing.Value('i', 0)  # shared integer between processes")
    shared = multiprocessing.Value("i", 42)
    print(f"Shared value: {shared.value}")
