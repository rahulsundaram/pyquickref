"""Tests for the example registry and lesson structure."""

from pyquickref.registry import (
    examples_for_lesson,
    examples_in_lesson_order,
    get_by_category,
    get_example,
    get_lesson,
    get_lessons,
    get_registry,
)


def test_registry_populated() -> None:
    """Registry should contain all registered examples."""
    registry = get_registry()
    assert len(registry) >= 46
    assert "basic_types" in registry
    assert "list_iterate" in registry
    assert "if_elif_else" in registry
    assert "function_basics" in registry
    assert "class_basics" in registry
    assert "factory_pattern" in registry
    assert "asyncio_example" in registry


def test_get_by_category() -> None:
    """Examples should be grouped by category."""
    groups = get_by_category()
    assert "Data Structures" in groups
    assert "Classes" in groups
    assert "Design Patterns" in groups
    assert len(groups["Data Structures"]) >= 12


def test_get_example_found() -> None:
    """Lookup should return ExampleInfo for known names."""
    info = get_example("loop_range")
    assert info is not None
    assert info.category == "Loops"
    assert info.doc_url != ""


def test_get_example_missing() -> None:
    """Lookup should return None for unknown names."""
    assert get_example("nonexistent_example") is None


def test_lessons_exist() -> None:
    """There should be at least 10 lessons in order."""
    lessons = get_lessons()
    assert len(lessons) >= 10
    assert lessons[0].number == 1
    assert lessons[0].title == "Data Structures"


def test_get_lesson_by_number() -> None:
    """Lookup a lesson by number."""
    lesson = get_lesson(1)
    assert lesson is not None
    assert lesson.title == "Data Structures"
    assert get_lesson(999) is None


def test_examples_for_lesson() -> None:
    """Each lesson should resolve to its examples."""
    lesson = get_lesson(1)
    assert lesson is not None
    examples = examples_for_lesson(lesson)
    names = [e.name for e in examples]
    assert "list_iterate" in names
    assert "dict_iterate" in names


def test_examples_in_lesson_order() -> None:
    """All examples should appear in lesson order without duplicates."""
    ordered = examples_in_lesson_order()
    names = [e.name for e in ordered]
    assert len(names) == len(set(names))
    assert len(names) >= 46
    # Lesson 1 examples should come before lesson 10 examples
    assert names.index("list_iterate") < names.index("factory_pattern")
