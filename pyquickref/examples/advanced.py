"""Advanced Python examples for PyQuickRef.

Regex, JSON operations, multithreading, and itertools.
"""

import concurrent.futures
import itertools
import json
import os
import re

from pyquickref.registry import example, show


@example(
    "Advanced",
    "json.dumps(), json.loads(), reading/writing JSON files",
    doc_url="https://docs.python.org/3/library/json.html",
    needs_output_dir=True,
)
def json_operations(output_dir: str) -> None:
    """Demonstrate JSON operations including serialization and deserialization."""
    person = {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "courses": ["Python", "Data Science", "Machine Learning"],
        "address": {"street": "123 Main St", "city": "Pythonville"},
    }

    # Convert to JSON string
    json_string = json.dumps(person, indent=2)
    show("json.dumps(person, indent=2)")
    print("Python to JSON:")
    print(json_string)

    # Parse JSON string back to Python
    parsed_json = json.loads(json_string)
    show("json.loads(json_string)")
    print("\nJSON to Python:")
    print(f"Name: {parsed_json['name']}")
    print(f"First course: {parsed_json['courses'][0]}")

    # Save to file
    output_path = os.path.join(output_dir, "person.json")
    try:
        with open(output_path, "w") as f:
            json.dump(person, f, indent=2)
        print(f"Saved JSON to {output_path}")
    except OSError as e:
        print(f"Error saving JSON to file: {e}")

    # Load example json if it exists
    example_json_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "data",
        "json_example.json",
    )
    if os.path.exists(example_json_path):
        try:
            with open(example_json_path) as f:
                example_data = json.load(f)
            print("\nLoaded example JSON data:")
            print(f"Name: {example_data.get('name')}")
            print(f"Description: {example_data.get('description')}")
            print(
                f"First example type: {example_data.get('examples', [])[0].get('type')}"
            )
        except (OSError, json.JSONDecodeError, KeyError, IndexError) as e:
            print(f"Error loading example JSON: {e}")


@example(
    "Advanced",
    "re.findall(), re.search(), re.sub() for text processing",
    doc_url="https://docs.python.org/3/library/re.html",
)
def regex_patterns() -> None:
    """Demonstrate the use of regular expressions in Python."""
    text = "Contact us at info@example.com or support@python.org"

    # Find all email addresses
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    show(r"re.findall(r'\b[A-Za-z0-9._%+-]+@...', text)")
    emails = re.findall(email_pattern, text)
    print(f"Emails found: {emails}")

    # Match pattern
    date_text = "Today's date is 2023-11-25"
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    show(r"re.search(r'\d{4}-\d{2}-\d{2}', text)")
    match = re.search(date_pattern, date_text)
    if match:
        print(f"Date found: {match.group()}")

    # Replace with regex
    show("re.sub(r'[email]+@', 'EMAIL@', text)")
    censored = re.sub(r"[A-Za-z0-9._%+-]+@", "EMAIL@", text)
    print(f"Censored text: {censored}")


@example(
    "Advanced",
    "combinations, permutations, product, cycle from itertools",
    doc_url="https://docs.python.org/3/library/itertools.html",
)
def itertools_examples() -> None:
    """Demonstrate the use of itertools functions in Python."""
    letters = ["A", "B", "C"]

    # Combinations
    show("itertools.combinations(['A', 'B', 'C'], 2)")
    print("Combinations of 2 from ABC:")
    for combo in itertools.combinations(letters, 2):
        print(combo)

    # Permutations
    show("itertools.permutations(['A', 'B', 'C'], 2)")
    print("\nPermutations of 2 from ABC:")
    for perm in itertools.permutations(letters, 2):
        print(perm)

    # Product
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    show("itertools.product(dice1, dice2)")
    print("\nSome possible dice rolls (first 5):")
    for roll in list(itertools.product(dice1, dice2))[:5]:
        roll_sum = sum(roll)
        print(f"Dice 1: {roll[0]}, Dice 2: {roll[1]}, Sum: {roll_sum}")

    # Cycle
    colors = ["red", "green", "blue"]
    show("itertools.cycle(['red', 'green', 'blue'])")
    color_cycle = itertools.cycle(colors)
    print("\nCycling through colors:")
    for _ in range(5):
        print(next(color_cycle))


@example(
    "Advanced",
    "ThreadPoolExecutor for concurrent task execution",
    doc_url="https://docs.python.org/3/library/concurrent.futures.html",
)
def thread_execute() -> None:
    """Demonstrate the use of multithreading in Python."""

    def task(n: int) -> str:
        return f"Task {n} completed"

    show(
        "with ThreadPoolExecutor() as executor:\n"
        "    results = executor.map(task, range(5))"
    )
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(task, range(5))
        for result in results:
            print(result)
