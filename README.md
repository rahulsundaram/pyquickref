# PyQuickRef

[![Run Tests](https://github.com/rahulsundaram/pyquickref/actions/workflows/run-tests.yml/badge.svg)](https://github.com/rahulsundaram/pyquickref/actions/workflows/run-tests.yml)
[![Lint](https://github.com/rahulsundaram/pyquickref/actions/workflows/lint.yml/badge.svg)](https://github.com/rahulsundaram/pyquickref/actions/workflows/lint.yml)

PyQuickRef is a Python reference tool showcasing practical examples of Python's most useful features. It serves as both a learning resource and a modern Python development workflow reference, including CI/CD with GitHub Actions, testing with pytest, type checking with [ty](https://github.com/astral-sh/ty), and code quality enforcement with ruff.

## Features

- **Interactive examples** for Python data structures and operations
- **Modular design** for running specific examples
- **Comprehensive coverage** of Python features:
  - Data structures: lists, dictionaries, sets, tuples
  - Collections: Counter, defaultdict, namedtuple, deque
  - String manipulation and formatting
  - Functional programming: lambda functions, map, filter, decorators
  - Modern Python: dataclasses, pattern matching, generators, enums
  - Regular expressions, file handling, JSON processing
  - Error handling with custom exceptions, context managers
  - Multithreading, itertools, loops (enumerate, zip, while)
- **Configurable output** with logging and output directory support
- **Complete test suite** ensuring reliability
- **Modern tooling**:
  - Type checking with [ty](https://github.com/astral-sh/ty)
  - Linting and formatting with ruff
  - Testing with pytest
  - CI/CD with GitHub Actions
  - Dependency management with uv

## Command-Line Options

PyQuickRef provides a flexible CLI for running examples:

```text
usage: Python Quick Reference Examples

options:
  -h, --help            Show this help message and exit.
  --functions FUNCTIONS [FUNCTIONS ...]
                        Specific functions to run.
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL,NONE}
                        Set logging level (default: INFO).
  --quiet               Suppress console output.
  --log-file LOG_FILE   Log to the specified file.
  --config CONFIG       Path to a YAML configuration file.
  --output-dir OUTPUT_DIR
                        Directory for file outputs (default: examples).
```

### Examples

#### Run All Examples

```bash
python main.py
```

#### Run Specific Examples

```bash
python main.py --functions list_iterate dict_iterate string_operations
```

#### Use a Configuration File

```bash
python main.py --config sample_config.yaml
```

#### Set Logging Level

```bash
python main.py --log-level DEBUG
```

#### Suppress Console Output

```bash
python main.py --quiet --log-file pyquickref.log
```

#### Specify Output Directory

```bash
python main.py --output-dir custom_output
```

## Installation

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/rahulsundaram/pyquickref.git
cd pyquickref
uv sync
```

## Usage

Run all examples:

```bash
python main.py
```

Run specific examples:

```bash
python main.py --functions list_iterate dict_iterate string_operations
```

Use a YAML configuration file:

```bash
python main.py --config sample_config.yaml
```

Control logging:

```bash
python main.py --log-level DEBUG
python main.py --quiet
```

Specify output directory:

```bash
python main.py --output-dir custom_output
```

## Function Groups

Examples are organized into the following groups:

- **Data Structures**: `list_iterate`, `list_modify`, `list_comprehend`, `dict_iterate`, `set_modify`, `tuple_unpack`, `conditional_check`
- **Collections**: `collections_example` (Counter, defaultdict, namedtuple, deque)
- **String Operations**: `string_operations`
- **Loops**: `loop_range` (range, enumerate, zip, while, break/continue)
- **Functional Programming**: `lambda_functions`, `decorator_example`, `itertools_examples`
- **Modern Python**: `dataclass_example`, `pattern_matching`, `generator_example`, `enum_example`
- **Error Handling**: `error_handle` (try/except/finally, custom exceptions)
- **File Operations**: `file_write`, `context_managers`
- **Advanced**: `regex_patterns`, `json_operations`, `thread_execute`

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
```

Or run individual tools directly:

```bash
uv run pytest tests/test_data_structures.py::test_list_iterate
```

### Code Style

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
