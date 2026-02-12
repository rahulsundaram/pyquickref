"""Collections module examples for PyQuickRef.

Counter, defaultdict, namedtuple, and deque.
Docs: https://docs.python.org/3/library/collections.html
"""

from collections import Counter, defaultdict, deque, namedtuple

from pyquickref.registry import example, show


@example(
    "Collections",
    "Counter, defaultdict, namedtuple, deque",
    doc_url="https://docs.python.org/3/library/collections.html",
)
def collections_example() -> None:
    """Demonstrate collections module data structures."""
    # Counter -- count occurrences
    words = ["the", "cat", "sat", "on", "the", "mat", "the", "cat"]
    word_counts = Counter(words)
    show("Counter(['the', 'cat', 'sat', 'on', 'the', 'mat', 'the', 'cat'])")
    print(f"Counter: {word_counts}")
    print(f"Most common 2: {word_counts.most_common(2)}")

    # defaultdict -- dict with default values
    show("grouped = defaultdict(list)\ngrouped['fruit'].append('apple')")
    grouped: defaultdict[str, list[str]] = defaultdict(list)
    items = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana"), ("veg", "pea")]
    for category, item in items:
        grouped[category].append(item)
    print(f"defaultdict: {dict(grouped)}")

    # namedtuple -- lightweight immutable record
    Person = namedtuple("Person", ["name", "age", "city"])
    alice = Person("Alice", 30, "NYC")
    show(
        "Person = namedtuple('Person', ['name', 'age', 'city'])\n"
        "alice = Person('Alice', 30, 'NYC')"
    )
    print(f"namedtuple: {alice}")
    print(f"  name={alice.name}, age={alice.age}")

    # deque -- fast appends/pops from both ends
    show("dq = deque([1, 2, 3], maxlen=5)\ndq.appendleft(0)\ndq.append(4)")
    dq: deque[int] = deque([1, 2, 3], maxlen=5)
    dq.appendleft(0)
    dq.append(4)
    print(f"deque: {dq}")
    dq.rotate(2)
    print(f"  rotated(2): {dq}")
