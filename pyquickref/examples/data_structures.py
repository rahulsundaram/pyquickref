"""Data structure examples for PyQuickRef.

Basic types, lists, dictionaries, sets, tuples, slicing, comprehensions.
Docs: https://docs.python.org/3/tutorial/datastructures.html
"""

import copy

from pyquickref.registry import example, show
from pyquickref.testdata import SampleData


@example(
    "Data Structures",
    "int, float, bool, None, type(), isinstance(), arithmetic",
    doc_url="https://docs.python.org/3/library/stdtypes.html",
)
def basic_types() -> None:
    """Demonstrate Python's basic data types and type operations."""
    # Numeric types
    show("x = 42\npi = 3.14\nis_valid = True\nnothing = None")
    x = 42
    pi = 3.14
    is_valid = True
    nothing = None
    print(f"int:   {x}  (type: {type(x).__name__})")
    print(f"float: {pi}  (type: {type(pi).__name__})")
    print(f"bool:  {is_valid}  (type: {type(is_valid).__name__})")
    print(f"None:  {nothing}  (type: {type(nothing).__name__})")

    # Arithmetic
    show(
        "10 / 3    # true division\n10 // 3   # floor division\n"
        "10 % 3    # modulo\n2 ** 10   # power"
    )
    print(f"10 / 3  = {10 / 3:.4f}")
    print(f"10 // 3 = {10 // 3}")
    print(f"10 % 3  = {10 % 3}")
    print(f"2 ** 10 = {2**10}")

    # Type conversion
    show('int("42")  str(3.14)  float("2.5")  bool(0)')
    print(f'int("42")  = {int("42")}')
    print(f"str(3.14)  = {str(3.14)!r}")
    print(f'float("2.5") = {float("2.5")}')
    print(f"bool(0)    = {bool(0)}, bool(1) = {bool(1)}")

    # isinstance
    show("isinstance(42, int)")
    print(f"isinstance(42, int)       = {isinstance(42, int)}")
    print(f"isinstance(42, int | str)  = {isinstance(42, int | str)}")


@example(
    "Data Structures",
    "List/string slicing, step, negative indices",
    doc_url="https://docs.python.org/3/library/stdtypes.html#common-sequence-operations",
)
def slice_operations() -> None:
    """Demonstrate slicing on lists and strings."""
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    show("nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
    print(f"nums = {nums}")

    show("nums[2:5]     # start:stop\nnums[:3]      # first 3\nnums[-3:]     # last 3")
    print(f"nums[2:5]  = {nums[2:5]}")
    print(f"nums[:3]   = {nums[:3]}")
    print(f"nums[-3:]  = {nums[-3:]}")

    show("nums[::2]     # every 2nd\nnums[::-1]    # reversed")
    print(f"nums[::2]  = {nums[::2]}")
    print(f"nums[::-1] = {nums[::-1]}")

    # String slicing
    s = "Hello, World!"
    show("s = 'Hello, World!'\ns[7:]     s[::-1]")
    print(f"s[7:]   = {s[7:]!r}")
    print(f"s[::-1] = {s[::-1]!r}")


@example(
    "Data Structures",
    "Dict comprehension, set comprehension, generator expression",
    doc_url="https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions",
)
def comprehensions() -> None:
    """Demonstrate dict, set, and generator comprehensions."""
    # Dict comprehension
    show("{x: x**2 for x in range(5)}")
    squares = {x: x**2 for x in range(5)}
    print(f"Dict comp: {squares}")

    # Dict comprehension with condition
    show("{k: v for k, v in scores.items() if v >= 80}")
    scores = {"Alice": 92, "Bob": 78, "Charlie": 85, "Diana": 65}
    passing = {k: v for k, v in scores.items() if v >= 80}
    print(f"Passing:   {passing}")

    # Set comprehension
    show("{len(w) for w in ['hello', 'world', 'hi', 'hey']}")
    lengths = {len(w) for w in ["hello", "world", "hi", "hey"]}
    print(f"Set comp:  {lengths}")

    # Generator expression (lazy)
    show("sum(x**2 for x in range(10))")
    total = sum(x**2 for x in range(10))
    print(f"Gen expr sum of squares: {total}")


@example(
    "Data Structures",
    "* unpacking, ** merging, swap, nested unpacking",
    doc_url="https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists",
)
def star_unpacking() -> None:
    """Demonstrate star unpacking and dict merging."""
    # Star unpacking
    show("first, *rest = [1, 2, 3, 4, 5]")
    first, *rest = [1, 2, 3, 4, 5]
    print(f"first = {first}, rest = {rest}")

    show("first, *middle, last = [1, 2, 3, 4, 5]")
    first, *middle, last = [1, 2, 3, 4, 5]
    print(f"first = {first}, middle = {middle}, last = {last}")

    # Dict merging with **
    show("merged = {**defaults, **overrides}")
    defaults = {"color": "blue", "size": "medium", "theme": "light"}
    overrides = {"size": "large", "theme": "dark"}
    merged = {**defaults, **overrides}
    print(f"Merged: {merged}")

    # | operator for dict merge (3.9+)
    show("merged = defaults | overrides")
    merged = defaults | overrides
    print(f"Merged (|): {merged}")

    # Variable swap
    show("a, b = b, a")
    a, b = 1, 2
    a, b = b, a
    print(f"After swap: a={a}, b={b}")


@example(
    "Data Structures",
    "is vs ==, shallow/deep copy, mutable default pitfall",
    doc_url="https://docs.python.org/3/library/copy.html",
)
def references_copies() -> None:
    """Demonstrate object identity, mutability, and copying."""
    # is vs == (identity vs equality)
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    show("a = [1, 2, 3]\nb = [1, 2, 3]\nc = a")
    print(f"a == b: {a == b}  (same value)")
    print(f"a is b: {a is b}  (different objects)")
    print(f"a is c: {a is c}  (same object)")

    # Mutation through shared reference
    show("c.append(4)")
    c.append(4)
    print(f"a = {a}  (also changed — c is a)")

    # Shallow vs deep copy
    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    show(
        "original = [[1, 2], [3, 4]]\n"
        "shallow = copy.copy(original)\n"
        "deep = copy.deepcopy(original)\n"
        "original[0].append(99)"
    )
    original[0].append(99)
    print(f"original: {original}")
    print(f"shallow:  {shallow}  (inner list shared!)")
    print(f"deep:     {deep}  (fully independent)")

    # Mutable default argument pitfall
    def bad_append(item: int, lst: list[int] = []) -> list[int]:  # noqa: B006
        lst.append(item)
        return lst

    show("def bad_append(item, lst=[]):\n    lst.append(item)\n    return lst")
    print(f"bad_append(1) = {bad_append(1)}")
    print(f"bad_append(2) = {bad_append(2)}  (same list reused!)")

    # The fix: use None as default
    show(
        "def good_append(item, lst=None):\n"
        "    if lst is None:\n"
        "        lst = []\n"
        "    lst.append(item)\n"
        "    return lst"
    )
    print("Fix: use None as default, create list inside function")


@example(
    "Data Structures",
    "Iterate through a list and print each item",
    doc_url="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists",
    needs_test_data=True,
)
def list_iterate(data: SampleData) -> None:
    """Iterate through the list and print each item."""
    show("for item in ['apple', 'banana', 'cherry']:\n    print(item)")
    for item in data.testlist:
        print(item)


@example(
    "Data Structures",
    "Check membership with 'in' operator",
    doc_url="https://docs.python.org/3/reference/expressions.html#membership-test-operations",
    needs_test_data=True,
)
def conditional_check(data: SampleData) -> None:
    """Check if a specific item exists in the list."""
    item = "banana"
    show(f"'{item}' in ['apple', 'banana', 'cherry']")
    if item in data.testlist:
        print(f"'{item}' is in the list!")
    else:
        print(f"'{item}' is not in the list.")


@example(
    "Data Structures",
    "Append, remove, and reverse a list",
    doc_url="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists",
    needs_test_data=True,
)
def list_modify(data: SampleData) -> None:
    """Modify the list by appending, removing, and reversing elements."""
    print("Original list:", data.testlist)

    data.testlist.append("four")
    show("testlist.append('four')")
    print("After appending 'four':", data.testlist)

    data.testlist.remove("banana")
    show("testlist.remove('banana')")
    print("After removing 'banana':", data.testlist)

    data.testlist.reverse()
    show("testlist.reverse()")
    print("After reversing:", data.testlist)


@example(
    "Data Structures",
    "Build lists concisely with list comprehensions",
    doc_url="https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions",
)
def list_comprehend() -> None:
    """Demonstrate list comprehension by creating a list of squares."""
    show("squares = [x**2 for x in range(5)]")
    squares = [x**2 for x in range(5)]
    print("List comprehension (squares):", squares)


@example(
    "Data Structures",
    "Iterate through dictionary key-value pairs",
    doc_url="https://docs.python.org/3/tutorial/datastructures.html#dictionaries",
    needs_test_data=True,
)
def dict_iterate(data: SampleData) -> None:
    """Iterate through the dictionary and print each key-value pair."""
    show(
        "for key, value in {'a': 1, 'b': 2, 'c': 3}.items():\n"
        "    print(f'Key: {key}, Value: {value}')"
    )
    for key, value in data.testdict.items():
        print(f"Key: {key}, Value: {value}")


@example(
    "Data Structures",
    "Add and remove elements from a set",
    doc_url="https://docs.python.org/3/tutorial/datastructures.html#sets",
    needs_test_data=True,
)
def set_modify(data: SampleData) -> None:
    """Modify the set by adding and removing elements."""
    print("Original set:", data.testset)

    data.testset.add(4)
    show("testset.add(4)")
    print("After adding 4:", data.testset)

    data.testset.remove(2)
    show("testset.remove(2)")
    print("After removing 2:", data.testset)


@example(
    "Data Structures",
    "Unpack tuple values into variables",
    doc_url="https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences",
    needs_test_data=True,
)
def tuple_unpack(data: SampleData) -> None:
    """Unpack a tuple into individual variables and print them."""
    show("a, b, c = (10, 20, 30)")
    a, b, c = data.testtuple
    print(f"Unpacked tuple values: a={a}, b={b}, c={c}")
