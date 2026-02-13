"""Tests for concurrency examples."""

from collections.abc import Callable

from pyquickref.examples.concurrency import (
    asyncio_example,
    multiprocessing_example,
    threading_example,
)


def test_asyncio_example(capture_output: Callable) -> None:
    """Test async/await and asyncio.gather."""
    output = capture_output(asyncio_example)
    assert "A done" in output
    assert "B done" in output
    assert "C done" in output


def test_threading_example(capture_output: Callable) -> None:
    """Test threading with locks and thread pools."""
    output = capture_output(threading_example)
    assert "Thread result:" in output
    assert "task-1 done" in output
    assert "Counter after 4 threads x 1000: 4000" in output
    assert "ThreadPool squares:" in output


def test_multiprocessing_example(capture_output: Callable) -> None:
    """Test multiprocessing and GIL explanation."""
    output = capture_output(multiprocessing_example)
    assert "GIL:" in output
    assert "I/O-bound" in output
    assert "CPU-bound" in output
    assert "ProcessPool cubes:" in output
    assert "Shared value: 42" in output
