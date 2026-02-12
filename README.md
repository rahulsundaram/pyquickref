# PyQuickRef

[![Run Tests](https://github.com/rahulsundaram/pyquickref/actions/workflows/run-tests.yml/badge.svg)](https://github.com/rahulsundaram/pyquickref/actions/workflows/run-tests.yml)
[![Lint](https://github.com/rahulsundaram/pyquickref/actions/workflows/lint.yml/badge.svg)](https://github.com/rahulsundaram/pyquickref/actions/workflows/lint.yml)

Learn Python by example — 46 examples across 10 lessons, from basic types to design patterns. Each example shows copy-pasteable code then output. Inspired by [Go by Example](https://gobyexample.com).

## Quick Start

```bash
git clone https://github.com/rahulsundaram/pyquickref.git
cd pyquickref
uv sync && source .venv/bin/activate
pyquickref                     # run all 10 lessons in order
pyquickref --list              # show the lesson plan
pyquickref --lesson 1          # run lesson 1 only
```

## Usage

```bash
pyquickref                          # run all lessons in order
pyquickref --lesson 3               # run lesson 3 (Functions)
pyquickref list_comprehend          # run one example by name
pyquickref factory_pattern asyncio_example   # run multiple examples
pyquickref --list                   # show the full lesson plan
pyquickref --config sample_config.yaml       # run examples from config
pyquickref --version                # show version
```

## Example Output

Each example shows indented, copy-pasteable code followed by its output:

```
############################################################
  Lesson 1: Data Structures
  Types, lists, dicts, sets, tuples, slicing, comprehensions
  https://docs.python.org/3/tutorial/datastructures.html
############################################################

--- list_comprehend ---
    Build lists concisely with list comprehensions
    https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

    squares = [x**2 for x in range(5)]

List comprehension (squares): [0, 1, 4, 9, 16]

--- list_iterate ---
    Iterate through a list and print each item
    https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

    for item in ['apple', 'banana', 'cherry']:
        print(item)

apple
banana
cherry
```

## Lessons

1. **Data Structures** ([docs](https://docs.python.org/3/tutorial/datastructures.html)) — `basic_types`, `slice_operations`, `comprehensions`, `star_unpacking`, `references_copies`, `list_iterate`, `conditional_check`, `list_modify`, `list_comprehend`, `dict_iterate`, `set_modify`, `tuple_unpack`
2. **Strings & Control Flow** ([docs](https://docs.python.org/3/tutorial/controlflow.html)) — `if_elif_else`, `for_while_loops`, `unicode_bytes`, `string_operations`, `loop_range`
3. **Functions** ([docs](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)) — `function_basics`, `builtin_functions`, `scope_closures`, `recursion_example`, `lambda_functions`, `decorator_example`
4. **Classes & OOP** ([docs](https://docs.python.org/3/tutorial/classes.html)) — `class_basics`, `dunder_methods`
5. **Error Handling** ([docs](https://docs.python.org/3/tutorial/errors.html)) — `error_handle`
6. **Collections & Itertools** ([docs](https://docs.python.org/3/library/collections.html)) — `collections_example`
7. **File I/O & Data Formats** ([docs](https://docs.python.org/3/tutorial/inputoutput.html)) — `file_write`, `context_managers`, `json_operations`, `regex_patterns`, `itertools_examples`, `thread_execute`
8. **Modern Python** ([docs](https://docs.python.org/3/whatsnew/3.10.html)) — `dataclass_example`, `pattern_matching`, `generator_example`, `enum_example`, `walrus_operator`, `type_hints`
9. **Standard Library** ([docs](https://docs.python.org/3/library/index.html)) — `pathlib_example`, `datetime_example`, `functools_example`, `asyncio_example`
10. **Design Patterns** ([docs](https://docs.python.org/3/library/abc.html)) — `factory_pattern`, `strategy_pattern`, `observer_pattern`

## Adding a New Example

Write a function, decorate it, done:

```python
# pyquickref/examples/my_module.py
from pyquickref.registry import example, show

@example(
    "My Category",
    "Short description of what this demonstrates",
    doc_url="https://docs.python.org/3/library/something.html",
)
def my_example() -> None:
    show("result = 1 + 1")
    print(f"result = {1 + 1}")
```

Then import the module in `pyquickref/examples/__init__.py`:

```python
from pyquickref.examples import my_module  # noqa: F401
```

That's it -- the `@example` decorator registers it automatically. No class, no `setattr`, no method list.

For examples that need shared test data or an output directory, use the flags:

```python
@example("Category", "desc", needs_test_data=True)
def uses_data(data: SampleData) -> None: ...

@example("Category", "desc", needs_output_dir=True)
def writes_files(output_dir: str) -> None: ...
```

## CLI Reference

```text
usage: pyquickref [-h] [-l] [-n N] [--config FILE] [--output-dir DIR] [-V]
                  [EXAMPLE ...]

positional arguments:
  EXAMPLE           examples to run (omit to run all lessons)

options:
  -h, --help        show this help message and exit
  -l, --list        show the lesson plan and all examples
  -n, --lesson N    run a specific lesson (e.g. --lesson 1)
  --config FILE     load examples to run from a YAML config file
  --output-dir DIR  directory for file outputs (default: data)
  -V, --version     show program's version number and exit
```

## Development

### Setup

```bash
uv sync              # install all dependencies
pre-commit install   # enable pre-commit hooks
```

### Running Checks

```bash
make check           # run all checks (lint + format + typecheck + test)
make lint            # ruff linter only
make format          # auto-format with ruff
make typecheck       # ty type checker only
make test            # pytest only
make run             # run all examples
make list            # list all examples
```

Or run individual tools directly:

```bash
uv run pytest tests/test_data_structures.py::test_list_iterate
```

### Toolchain

This project uses the [Astral](https://astral.sh/) toolchain:

- [uv](https://docs.astral.sh/uv/) for dependency management
- [ruff](https://docs.astral.sh/ruff/) for linting and formatting
- [ty](https://docs.astral.sh/ty/) for type checking

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Run `make check` to verify all checks pass
4. Commit and push
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.
