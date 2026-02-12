"""Loop examples for PyQuickRef.

For loops, while loops, enumerate, zip, and break/continue.
Docs: https://docs.python.org/3/tutorial/controlflow.html#for-statements
"""

from pyquickref.registry import example, show


@example(
    "Loops",
    "enumerate(), zip() — iterate with indices and parallel sequences",
    doc_url="https://docs.python.org/3/tutorial/controlflow.html#for-statements",
)
def loop_range() -> None:
    """Demonstrate for loops with range, enumerate, and zip."""
    # Basic range
    show("list(range(5))")
    print("Range(5):", list(range(5)))

    # Enumerate -- index + value
    fruits = ["apple", "banana", "cherry"]
    show("for i, fruit in enumerate(fruits):\n    print(f'  {i}: {fruit}')")
    print("Enumerate:")
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")

    # Zip -- iterate multiple sequences together
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    show("for name, age in zip(names, ages):\n    print(f'  {name} is {age}')")
    print("Zip:")
    for name, age in zip(names, ages, strict=False):
        print(f"  {name} is {age}")

    # While loop with break
    show("while count < 10:\n    if count == 3: break")
    print("While loop (break at 3):")
    count = 0
    while count < 10:
        if count == 3:
            break
        print(f"  count={count}")
        count += 1

    # Continue -- skip even numbers
    show("for i in range(6):\n    if i % 2 == 0: continue\n    print(i)")
    print("Continue (skip even):")
    for i in range(6):
        if i % 2 == 0:
            continue
        print(f"  {i}")
