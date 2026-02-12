"""Core runner for PyQuickRef.

Iterates the example registry and executes functions with the right arguments.
"""

import os

from pyquickref.registry import (
    ExampleInfo,
    Lesson,
    examples_for_lesson,
    examples_in_lesson_order,
    get_lessons,
    get_registry,
)
from pyquickref.testdata import SampleData


def _run_one(info: ExampleInfo, output_dir: str) -> None:
    """Execute a single example, injecting SampleData / output_dir as needed."""
    kwargs: dict[str, object] = {}
    if info.needs_test_data:
        kwargs["data"] = SampleData()
    if info.needs_output_dir:
        kwargs["output_dir"] = output_dir
    info.func(**kwargs)


def _print_lesson_header(lesson: Lesson) -> None:
    print(f"\n{'#' * 60}")
    print(f"  Lesson {lesson.number}: {lesson.title}")
    print(f"  {lesson.goal}")
    if lesson.doc_url:
        print(f"  {lesson.doc_url}")
    print(f"{'#' * 60}")


def _print_example_header(info: ExampleInfo) -> None:
    print(f"\n--- {info.name} ---")
    print(f"    {info.description}")
    if info.doc_url:
        print(f"    {info.doc_url}")


def run_lesson(lesson: Lesson, output_dir: str) -> None:
    """Run all examples in a single lesson."""
    os.makedirs(output_dir, exist_ok=True)
    _print_lesson_header(lesson)
    for info in examples_for_lesson(lesson):
        _print_example_header(info)
        _run_one(info, output_dir)
    print()


def run_examples(
    functions_to_run: list[str] | None = None, output_dir: str = "data"
) -> None:
    """Run selected examples (or all in lesson order)."""
    os.makedirs(output_dir, exist_ok=True)
    registry = get_registry()

    if functions_to_run:
        for name in functions_to_run:
            info = registry.get(name)
            if info is None:
                print(f"Warning: '{name}' not found in registry — skipping.")
                continue
            _print_example_header(info)
            _run_one(info, output_dir)
    else:
        current_lesson: int | None = None
        lessons = {cat: lesson for lesson in get_lessons() for cat in lesson.categories}
        for info in examples_in_lesson_order():
            lesson = lessons.get(info.category)
            lesson_num = lesson.number if lesson else None
            if lesson_num != current_lesson:
                current_lesson = lesson_num
                if lesson:
                    _print_lesson_header(lesson)
            _print_example_header(info)
            _run_one(info, output_dir)

    print()


def list_examples() -> None:
    """Print all lessons and their examples."""
    lessons = get_lessons()
    total = sum(len(examples_for_lesson(ls)) for ls in lessons)
    print(f"\n{total} examples across {len(lessons)} lessons:\n")

    for lesson in lessons:
        print(f"  Lesson {lesson.number}: {lesson.title}")
        print(f"  {lesson.goal}")
        if lesson.doc_url:
            print(f"  {lesson.doc_url}")
        print()
        for info in examples_for_lesson(lesson):
            print(f"    {info.name:30s} {info.description}")
        print()
