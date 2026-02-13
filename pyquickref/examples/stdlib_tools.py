"""Standard library tools examples for PyQuickRef.

pathlib, datetime/zoneinfo, functools, logging, subprocess.
"""

import logging
import subprocess
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
    @lru_cache(maxsize=128)
    def fib(n: int) -> int:
        """Return the nth Fibonacci number."""
        return n if n < 2 else fib(n - 1) + fib(n - 2)

    show(fib)
    print(f"fib(10) = {fib(10)}")
    print(f"cache_info: {fib.cache_info()}")

    # partial
    show("double = partial(mul, 2)")

    def mul(a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b

    double = partial(mul, 2)
    print(f"double(5) = {double(5)}")

    # reduce
    show("reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])")
    total = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
    print(f"reduce sum = {total}")


@example(
    "Stdlib Tools",
    "Logging module: loggers, handlers, formatters, levels",
    doc_url="https://docs.python.org/3/library/logging.html",
)
def logging_example() -> None:
    """Demonstrate the logging module with handlers and formatters."""
    import io

    show(
        "logger = logging.getLogger('myapp')\n"
        "handler = logging.StreamHandler(stream)\n"
        "handler.setFormatter(logging.Formatter(fmt))\n"
        "logger.addHandler(handler)"
    )

    # Create a logger with a stream handler that writes to a StringIO
    # so we can capture and display the output
    stream = io.StringIO()
    logger = logging.getLogger("pyquickref.demo")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    fmt = "%(levelname)-8s %(name)s: %(message)s"
    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)

    show(
        "logger.debug('Detailed info for diagnosing')\n"
        "logger.info('General operational message')\n"
        "logger.warning('Something unexpected')\n"
        "logger.error('Something failed')"
    )
    logger.debug("Detailed info for diagnosing")
    logger.info("General operational message")
    logger.warning("Something unexpected")
    logger.error("Something failed")

    output = stream.getvalue()
    for line in output.strip().splitlines():
        print(f"  {line}")

    # Levels hierarchy
    show(
        "logging.DEBUG < logging.INFO < logging.WARNING"
        " < logging.ERROR < logging.CRITICAL"
    )
    print(
        f"DEBUG={logging.DEBUG}, INFO={logging.INFO}, WARNING={logging.WARNING}, "
        f"ERROR={logging.ERROR}, CRITICAL={logging.CRITICAL}"
    )

    # Cleanup
    logger.handlers.clear()


@example(
    "Stdlib Tools",
    "subprocess.run: execute commands, capture output, check errors",
    doc_url="https://docs.python.org/3/library/subprocess.html",
)
def subprocess_example() -> None:
    """Demonstrate subprocess.run for executing external commands."""
    show("result = subprocess.run(['echo', 'hello'], capture_output=True, text=True)")
    result = subprocess.run(
        ["echo", "hello"],
        capture_output=True,
        text=True,
        check=False,
    )
    print(f"stdout     : {result.stdout.strip()!r}")
    print(f"returncode : {result.returncode}")

    show(
        "result = subprocess.run(\n"
        "    ['python3', '-c', 'print(2+2)'],\n"
        "    capture_output=True, text=True)"
    )
    result = subprocess.run(
        ["python3", "-c", "print(2+2)"],
        capture_output=True,
        text=True,
        check=False,
    )
    print(f"stdout     : {result.stdout.strip()!r}")

    # check=True raises on non-zero exit
    show(
        "try:\n"
        "    subprocess.run(['false'], check=True)\n"
        "except subprocess.CalledProcessError as e:\n"
        "    print(f'Command failed: {e}')"
    )
    try:
        subprocess.run(["false"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: exit code {e.returncode}")
