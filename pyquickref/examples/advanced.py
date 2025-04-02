"""Advanced Python examples for PyQuickRef.

This module contains examples demonstrating advanced Python features,
including regex, JSON operations, multithreading, and itertools.
"""

import concurrent.futures
import itertools
import json
import os
import re
from typing import Any


def json_operations(self: Any) -> None:
    """Demonstrate JSON operations including serialization and deserialization."""
    self.logger.info("Demonstrating JSON operations")
    # Create Python object
    person = {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "courses": ["Python", "Data Science", "Machine Learning"],
        "address": {"street": "123 Main St", "city": "Pythonville"},
    }
    self.logger.debug(f"Created test person object: {person}")

    # Convert to JSON string
    json_string = json.dumps(person, indent=2)
    self.logger.debug("Converted person to JSON string")
    print("Python to JSON:")
    print(json_string)

    # Parse JSON string back to Python
    parsed_json = json.loads(json_string)
    self.logger.debug("Parsed JSON string back to Python object")
    print("\nJSON to Python:")
    print(f"Name: {parsed_json['name']}")
    print(f"First course: {parsed_json['courses'][0]}")

    # Save to file if output directory is set
    if self.output_dir:
        output_path = self._get_output_path("person.json")
        try:
            with open(output_path, "w") as f:
                json.dump(person, f, indent=2)
            print(f"Saved JSON to {output_path}")
        except Exception as e:
            self.logger.error(f"Error saving JSON to file: {str(e)}")

    # Load example json if it exists
    example_json_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "examples",
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
        except Exception as e:
            self.logger.error(f"Error loading example JSON: {str(e)}")


def regex_patterns(self: Any) -> None:
    """Demonstrate the use of regular expressions in Python."""
    self.logger.info("Demonstrating regular expressions")
    text = "Contact us at info@example.com or support@python.org"
    self.logger.debug(f"Sample text for regex: {text}")

    # Find all email addresses
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    self.logger.debug(f"Using email pattern: {email_pattern}")
    emails = re.findall(email_pattern, text)
    self.logger.info(f"Emails found: {emails}")
    print(f"Emails found: {emails}")

    # Match pattern
    date_text = "Today's date is 2023-11-25"
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    self.logger.debug(f"Looking for date pattern {date_pattern} in '{date_text}'")
    match = re.search(date_pattern, date_text)
    if match:
        self.logger.info(f"Date found: {match.group()}")
        print(f"Date found: {match.group()}")

    # Replace with regex
    censored = re.sub(r"[A-Za-z0-9._%+-]+@", "EMAIL@", text)
    self.logger.debug(f"Text after email censoring: {censored}")
    print(f"Censored text: {censored}")


def itertools_examples(self: Any) -> None:
    """Demonstrate the use of itertools functions in Python."""
    self.logger.info("Demonstrating itertools functions")
    # Combinations
    letters = ["A", "B", "C"]
    self.logger.debug(f"Finding combinations of {letters}")
    print("Combinations of 2 from ABC:")
    for combo in itertools.combinations(letters, 2):
        self.logger.debug(f"Combination: {combo}")
        print(combo)

    # Permutations
    self.logger.debug(f"Finding permutations of {letters}")
    print("\nPermutations of 2 from ABC:")
    for perm in itertools.permutations(letters, 2):
        self.logger.debug(f"Permutation: {perm}")
        print(perm)

    # Product
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    self.logger.debug("Calculating product of dice rolls")
    print("\nSome possible dice rolls (first 5):")
    for roll in list(itertools.product(dice1, dice2))[:5]:
        roll_sum = sum(roll)
        self.logger.debug(f"Dice roll: {roll}, Sum: {roll_sum}")
        print(f"Dice 1: {roll[0]}, Dice 2: {roll[1]}, Sum: {roll_sum}")

    # Cycle
    colors = ["red", "green", "blue"]
    self.logger.debug(f"Creating cycle from {colors}")
    color_cycle = itertools.cycle(colors)
    print("\nCycling through colors:")
    for _ in range(5):
        color = next(color_cycle)
        self.logger.debug(f"Next color in cycle: {color}")
        print(color)


def thread_execute(self: Any) -> None:
    """Demonstrate the use of multithreading in Python."""
    self.logger.info("Demonstrating thread execution")

    def task(n: int) -> str:
        self.logger.debug(f"Task {n} started")
        result = f"Task {n} completed"
        self.logger.debug(result)
        return result

    self.logger.debug("Creating thread pool executor")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(task, range(5))
        for result in results:
            print(result)
