# PyQuickRef

[![Run Tests](https://github.com/rahulsundaram/pyquickref/actions/workflows/run-tests.yml/badge.svg)](https://github.com/rahulsundaram/pyquickref/actions/workflows/run-tests.yml)
[![Lint](https://github.com/rahulsundaram/pyquickref/actions/workflows/lint.yml/badge.svg)](https://github.com/rahulsundaram/pyquickref/actions/workflows/lint.yml)
[![Security Scan](https://github.com/rahulsundaram/pyquickref/actions/workflows/security.yml/badge.svg)](https://github.com/rahulsundaram/pyquickref/actions/workflows/security.yml)

PyQuickRef is a comprehensive Python reference tool that demonstrates Python's most useful features through practical examples. Whether you're learning Python or need a quick refresher, PyQuickRef provides runnable examples covering a wide range of Python functionality.

This project also serves as a reference implementation for modern Python tooling and development workflows, including GitHub Actions CI/CD, testing with pytest, type checking with mypy, and code quality enforcement with ruff.

## Features

- **Interactive examples** for Python data structures and operations
- **Modular design** allows running specific examples as needed
- **Comprehensive coverage** of Python features:
  - Lists, dictionaries, sets, and tuples
  - String manipulation and formatting
  - Lambda functions and comprehensions
  - Regular expressions
  - File handling
  - JSON processing
  - Error handling
  - Context managers
  - Decorators
  - Multithreading
  - Itertools utilities
- **Configurable output** with logging and output directory support
- **Complete test suite** ensuring all examples work as expected
- **Modern development tooling** showcasing:
  - Type checking with mypy
  - Linting and formatting with ruff
  - Testing with pytest
  - CI/CD with GitHub Actions
  - Dependency management with uv

## Installation

### Using uv (recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver that can significantly speed up dependency installation:

```bash
# Install uv if you don't have it
pip install uv

# Clone the repository
git clone https://github.com/rahulsundaram/pyquickref.git
cd pyquickref

# Install dependencies with uv
uv sync
```

### Using pip (alternative)

```bash
# Clone the repository
git clone https://github.com/rahulsundaram/pyquickref.git
cd pyquickref

# Install dependencies
pip install -e .
```

## Usage

### Running All Examples

To run all examples:

```bash
python main.py
```

If no functions are specified either via command line or config file, the program will automatically run all available examples.

### Running Specific Examples

To run specific functions:

```bash
python main.py --functions list_iterate dict_iterate string_operations
```

### Using a Configuration File

You can specify which functions to run in a YAML configuration file:

```bash
python main.py --config sample_config.yaml
```

See `sample_config.yaml` for an example configuration.

### Controlling Logging

Set the logging level:

```bash
python main.py --log-level DEBUG
```

Available log levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`, `NONE`

Disable console logging output:

```bash
python main.py --quiet
```

### Output Directory

By default, file outputs go to the `examples` directory. You can specify a different directory:

```bash
python main.py --output-dir custom_output
```

## Configuration Examples

### Basic Usage

Run all examples with default settings:

```bash
python main.py
```

### Custom Selection with Detailed Logging

Run selected examples with debug logging:

```bash
python main.py --functions lambda_functions regex_patterns json_operations --log-level DEBUG
```

### Using Config File with Alternative Output

Run examples defined in a config file with a custom output directory:

```bash
python main.py --config sample_config.yaml --output-dir custom_output
```

## Function Groups

The examples are organized into the following groups:

### Data Structures

- `list_iterate` - Basic list iteration
- `list_modify` - List modification methods
- `list_comprehend` - List comprehensions
- `dict_iterate` - Dictionary usage
- `set_modify` - Set operations
- `tuple_unpack` - Tuple unpacking

### String Operations

- `string_operations` - String manipulation and formatting

### Functional Programming

- `lambda_functions` - Lambda expressions with map, filter, and sorting

### Error Handling

- `error_handle` - Try-except blocks and exception handling

### File Operations

- `file_write` - File writing operations
- `context_managers` - Using context managers for resource handling

### Advanced Features

- `regex_patterns` - Regular expression patterns and matching
- `json_operations` - JSON serialization and parsing
- `decorator_example` - Creating and using decorators
- `thread_execute` - Basic multithreading with concurrent.futures
- `itertools_examples` - Using Python's itertools library

## Examples Directory

The `examples/` directory contains sample files and outputs from the PyQuickRef functions. These files are used for demonstration and testing purposes.

## Development

### Setting up the Development Environment

To set up your development environment, run:

chmod +x scripts/setup_dev.sh

```bash
# Run the setup script
./scripts/setup_dev.sh
```

This will:

- Install all development dependencies
- Set up pre-commit hooks
- Make the test scripts executable

### Project Structure

PyQuickRef is organized as a proper Python package:

### Running Tests and Linting

You can run all tests and linting with a single command:

```bash
./scripts/run_tests.sh
```

This script will:

1. Run type checking with mypy
2. Check code formatting with ruff
3. Run linting with ruff
4. Execute all tests with pytest

#### Running Only Unit Tests

If you want to run just the Python unit tests without the linting and type checking:

```bash
# Run all tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run a specific test file
uv run pytest tests/test_data_structures.py

# Run a specific test function
uv run pytest tests/test_data_structures.py::test_list_iterate
```

Using pytest directly gives you more granular control over which tests to run and how to run them.

#### Test Configuration

PyQuickRef uses a `pytest.ini` file to configure pytest behavior. This configuration:

- Sets test discovery paths (`testpaths = tests`)
- Specifies test file naming conventions (`python_files = test_*.py`)
- Configures test class naming patterns (`python_classes = Test*`)
- Configures test function naming patterns (`python_functions = test_*`)
- Sets default command-line options (`addopts = -v`)

### Test Organization

Tests are organized by functionality:

- `test_data_structures.py`: Tests for lists, dictionaries, sets, and tuples
- `test_string_operations.py`: Tests for string manipulation
- `test_functional.py`: Tests for functional programming features
- `test_file_operations.py`: Tests for file handling and context managers
- `test_advanced.py`: Tests for advanced features like regex, JSON, and threading

### Code Style

This project uses:

- [uv](https://github.com/astral-sh/uv) for managing dependencies and running scripts
- [Ruff](https://github.com/astral-sh/ruff) for code formatting, linting, and style enforcement
- mypy for type checking

#### Using uv

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Type checking
uv run mypy .
```

### Why uv?

[uv](https://github.com/astral-sh/uv) offers several advantages over traditional pip:

- **Speed**: Much faster installation of packages
- **Caching**: Better dependency caching
- **Reliability**: Improved dependency resolution
- **Compatibility**: Drop-in replacement for pip

### Why Ruff?

[Ruff](https://github.com/astral-sh/ruff) replaces multiple tools (Black, Flake8, isort) with a single, fast linter and formatter:

- **Speed**: 10-100x faster than alternatives
- **Comprehensive**: Includes 700+ rules from various linters
- **Configurable**: Highly configurable to match your preferences
- **Drop-in replacement**: Compatible with Black formatting style

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (after formatting with `ruff format .`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
