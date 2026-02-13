"""Testing and debugging examples for PyQuickRef.

pytest patterns, fixtures, parametrize, mocking, pdb/breakpoint.
Docs: https://docs.python.org/3/library/unittest.html
"""

import traceback

from pyquickref.registry import example, show


@example(
    "Testing & Debugging",
    "pytest patterns: fixtures, parametrize, markers, assertions",
    doc_url="https://docs.pytest.org/en/stable/",
)
def pytest_example() -> None:
    """Demonstrate pytest patterns as code examples (not actually invoking pytest)."""
    # Basic test structure
    show(
        "# test_math.py\n"
        "def test_addition():\n"
        "    assert 1 + 1 == 2\n"
        "    assert 0.1 + 0.2 == pytest.approx(0.3)\n\n"
        "def test_exception():\n"
        "    with pytest.raises(ZeroDivisionError):\n"
        "        1 / 0"
    )
    print("pytest.raises catches expected exceptions")
    print(f"  1 + 1 == 2: {1 + 1 == 2}")

    # Fixtures
    show(
        "@pytest.fixture\n"
        "def db_connection():\n"
        '    conn = connect("test.db")\n'
        "    yield conn          # setup above, teardown below\n"
        "    conn.close()\n\n"
        "def test_query(db_connection):\n"
        '    result = db_connection.execute("SELECT 1")\n'
        "    assert result == 1"
    )
    print("Fixtures provide setup/teardown via yield")

    # Parametrize
    show(
        '@pytest.mark.parametrize("x, expected", [\n'
        "    (1, 1),\n"
        "    (2, 4),\n"
        "    (3, 9),\n"
        "])\n"
        "def test_square(x, expected):\n"
        "    assert x ** 2 == expected"
    )
    test_cases = [(1, 1), (2, 4), (3, 9)]
    for x, expected in test_cases:
        result = x**2
        status = "PASS" if result == expected else "FAIL"
        print(f"  {x}**2 = {result}, expected {expected}: {status}")

    # Markers
    show(
        "@pytest.mark.slow\n"
        "def test_big_computation():\n"
        "    ...\n\n"
        "# Run: pytest -m 'not slow'     # skip slow tests\n"
        "# Run: pytest -k 'test_square'  # run tests matching name"
    )
    print("Markers: @pytest.mark.slow, @pytest.mark.skip, @pytest.mark.xfail")

    # Mocking
    show(
        "from unittest.mock import patch, MagicMock\n\n"
        "@patch('mymodule.requests.get')\n"
        "def test_api_call(mock_get):\n"
        "    mock_get.return_value.json.return_value = {'key': 'value'}\n"
        "    result = mymodule.fetch_data()\n"
        "    assert result == {'key': 'value'}\n"
        "    mock_get.assert_called_once()"
    )
    from unittest.mock import MagicMock

    mock = MagicMock()
    mock.return_value = 42
    print(f"MagicMock()() = {mock()}")
    print(f"mock.called = {mock.called}")
    print(f"mock.call_count = {mock.call_count}")


@example(
    "Testing & Debugging",
    "Debugging: breakpoint(), pdb commands, traceback module",
    doc_url="https://docs.python.org/3/library/pdb.html",
)
def debugging_example() -> None:
    """Demonstrate debugging tools and techniques."""
    # Breakpoint and pdb usage
    show(
        "# Insert a breakpoint in your code:\n"
        "def buggy_function(x):\n"
        "    breakpoint()        # drops into pdb (Python 3.7+)\n"
        "    return x * 2\n\n"
        "# pdb commands:\n"
        "#   n (next)     — execute next line\n"
        "#   s (step)     — step into function call\n"
        "#   c (continue) — continue until next breakpoint\n"
        "#   p expr       — print expression\n"
        "#   l (list)     — show source around current line\n"
        "#   w (where)    — show call stack\n"
        "#   q (quit)     — exit debugger"
    )
    print("breakpoint() is equivalent to import pdb; pdb.set_trace()")
    print("Set PYTHONBREAKPOINT=0 to disable all breakpoints")

    # traceback module
    show(
        "import traceback\n\n"
        "try:\n"
        "    1 / 0\n"
        "except ZeroDivisionError:\n"
        "    traceback.print_exc()       # print full traceback\n"
        "    tb_str = traceback.format_exc()  # get as string"
    )
    try:
        _ = 1 / 0
    except ZeroDivisionError:
        tb_str = traceback.format_exc()
        # Show just the last 2 lines (exception info)
        lines = tb_str.strip().splitlines()
        print(f"traceback.format_exc() last line: {lines[-1]!r}")

    # assert with messages
    show(
        "# Assert with descriptive messages:\n"
        "assert len(items) > 0, 'items list must not be empty'\n"
        "assert isinstance(x, int), f'expected int, got {type(x).__name__}'\n\n"
        "# Disable assertions with: python -O script.py"
    )
    x = 42
    assert isinstance(x, int), f"expected int, got {type(x).__name__}"
    print("assert isinstance(42, int) passed")
    print("python -O disables assert statements (optimized mode)")

    # __debug__ flag
    show(
        "if __debug__:\n"
        "    print('Debug mode — assertions are active')\n"
        "# __debug__ is True unless python -O is used"
    )
    print(f"__debug__ = {__debug__}")
