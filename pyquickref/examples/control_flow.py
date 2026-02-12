"""Control flow examples for PyQuickRef.

if/elif/else, ternary expressions, for loops, while loops.
Docs: https://docs.python.org/3/tutorial/controlflow.html
"""

from pyquickref.registry import example, show


@example(
    "Control Flow",
    "if/elif/else, ternary expressions, truthiness",
    doc_url="https://docs.python.org/3/tutorial/controlflow.html#if-statements",
)
def if_elif_else() -> None:
    """Demonstrate if/elif/else, ternary, and truthiness."""
    # Basic if/elif/else
    score = 85
    show(
        "score = 85\n"
        "if score >= 90:\n"
        "    grade = 'A'\n"
        "elif score >= 80:\n"
        "    grade = 'B'\n"
        "elif score >= 70:\n"
        "    grade = 'C'\n"
        "else:\n"
        "    grade = 'F'"
    )
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"score={score} → grade={grade}")

    # Ternary (conditional expression)
    age = 20
    show("status = 'adult' if age >= 18 else 'minor'")
    status = "adult" if age >= 18 else "minor"
    print(f"age={age} → status={status}")

    # Truthiness — what evaluates to False
    show(
        "for val in [0, '', [], None, False, 1, 'hi', [1]]:\n"
        "    print(f'{str(val):6s} → {bool(val)}')"
    )
    print("Truthiness:")
    for val in [0, "", [], None, False, 1, "hi", [1]]:
        print(f"  {str(val):6s} → {bool(val)}")


@example(
    "Control Flow",
    "for loops, while loops, range, break, continue",
    doc_url="https://docs.python.org/3/tutorial/controlflow.html#for-statements",
)
def for_while_loops() -> None:
    """Demonstrate basic for and while loops."""
    # For loop over a list
    show("colors = ['red', 'green', 'blue']\nfor color in colors:\n    print(color)")
    for color in ["red", "green", "blue"]:
        print(color)

    # For loop with range
    show("for i in range(5):\n    print(i, end=' ')")
    print("range(5):", end=" ")
    for i in range(5):
        print(i, end=" ")
    print()

    # While loop
    show("n = 1\nwhile n <= 16:\n    print(n, end=' ')\n    n *= 2")
    print("Powers of 2:", end=" ")
    n = 1
    while n <= 16:
        print(n, end=" ")
        n *= 2
    print()

    # Break — exit early
    show("for i in range(10):\n    if i == 5: break\n    print(i, end=' ')")
    print("Break at 5:", end=" ")
    for i in range(10):
        if i == 5:
            break
        print(i, end=" ")
    print()

    # Continue — skip iterations
    show("for i in range(6):\n    if i % 2 == 0: continue\n    print(i, end=' ')")
    print("Odd only:", end=" ")
    for i in range(6):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()
