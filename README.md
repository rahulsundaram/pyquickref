# PyQuickRef

[![Run Tests](https://github.com/rahulsundaram/pyquickref/actions/workflows/run-tests.yml/badge.svg)](https://github.com/rahulsundaram/pyquickref/actions/workflows/run-tests.yml)
[![Lint](https://github.com/rahulsundaram/pyquickref/actions/workflows/lint.yml/badge.svg)](https://github.com/rahulsundaram/pyquickref/actions/workflows/lint.yml)

PyQuickRef is a Python reference tool showcasing practical examples of Python's most useful features. It serves as both a learning resource and a modern Python development workflow reference, including CI/CD with GitHub Actions, testing with pytest, type checking with mypy, and code quality enforcement with ruff.

## Features

- **Interactive examples** for Python data structures and operations
- **Modular design** for running specific examples
- **Comprehensive coverage** of Python features:
  - Data structures: lists, dictionaries, sets, tuples
  - String manipulation and formatting
  - Functional programming: lambda functions, comprehensions
  - Regular expressions, file handling, JSON processing
  - Error handling, context managers, decorators
  - Multithreading, itertools utilities
- **Configurable output** with logging and output directory support
- **Complete test suite** ensuring reliability
- **Modern tooling**:
  - Type checking with mypy
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

### Using uv (recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer:

```bash
pip install uv
git clone https://github.com/rahulsundaram/pyquickref.git
cd pyquickref
uv sync
```

### Using pip (alternative)

```bash
git clone https://github.com/rahulsundaram/pyquickref.git
cd pyquickref
pip install -e .
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

- **Data Structures**: `list_iterate`, `list_modify`, `dict_iterate`, etc.
- **String Operations**: `string_operations`
- **Functional Programming**: `lambda_functions`
- **Error Handling**: `error_handle`
- **File Operations**: `file_write`, `context_managers`
- **Advanced Features**: `regex_patterns`, `json_operations`, `decorator_example`, etc.

## Development

### Setting up the Development Environment

Run the setup script:

```bash
chmod +x scripts/setup_dev.sh
./scripts/setup_dev.sh
```

This installs dependencies, sets up pre-commit hooks, and makes test scripts executable.

### Running Tests and Linting

Run all tests and linting:

```bash
./scripts/run_tests.sh
```

Run specific tests:

```bash
uv run pytest
uv run pytest -v
uv run pytest tests/test_data_structures.py::test_list_iterate
```

### Code Style

This project uses:

- [uv](https://github.com/astral-sh/uv) for dependency management
- [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
- mypy for type checking

Commands:

```bash
uv run ruff format .
uv run ruff check .
uv run mypy .
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (format with `ruff format .`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.
