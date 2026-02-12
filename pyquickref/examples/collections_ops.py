"""Collections module examples for PyQuickRef.

This module demonstrates useful data structures from the collections module:
Counter, defaultdict, namedtuple, and deque.
"""

from collections import Counter, defaultdict, deque, namedtuple
from typing import Any


def collections_example(self: Any) -> None:
    """Demonstrate collections module data structures."""
    self.logger.info("Demonstrating collections module")

    # Counter — count occurrences
    words = ["the", "cat", "sat", "on", "the", "mat", "the", "cat"]
    word_counts = Counter(words)
    print(f"Counter: {word_counts}")
    print(f"Most common 2: {word_counts.most_common(2)}")

    # defaultdict — dict with default values
    grouped: defaultdict[str, list[str]] = defaultdict(list)
    items = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana"), ("veg", "pea")]
    for category, item in items:
        grouped[category].append(item)
    print(f"defaultdict: {dict(grouped)}")

    # namedtuple — lightweight immutable record
    Person = namedtuple("Person", ["name", "age", "city"])
    alice = Person("Alice", 30, "NYC")
    print(f"namedtuple: {alice}")
    print(f"  name={alice.name}, age={alice.age}")

    # deque — fast appends/pops from both ends
    dq: deque[int] = deque([1, 2, 3], maxlen=5)
    dq.appendleft(0)
    dq.append(4)
    print(f"deque: {dq}")
    dq.rotate(2)
    print(f"  rotated(2): {dq}")
