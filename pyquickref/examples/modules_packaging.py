"""Modules and packaging examples for PyQuickRef.

Import system, __init__.py, __all__, __name__, entry points, pyproject.toml.
Docs: https://docs.python.org/3/reference/import.html
"""

import sys

from pyquickref.registry import example, show


@example(
    "Modules & Packaging",
    "Import system: absolute/relative imports, __init__.py, __all__, sys.path",
    doc_url="https://docs.python.org/3/reference/import.html",
)
def import_system() -> None:
    """Demonstrate the Python import system and module mechanics."""
    # Import styles
    show(
        "# Absolute imports (preferred)\n"
        "import os\n"
        "from os.path import join\n"
        "from collections import defaultdict\n\n"
        "# Relative imports (inside packages only)\n"
        "from . import sibling_module\n"
        "from ..parent import something\n"
        "from .utils import helper"
    )
    print("Absolute imports use the full package path")
    print("Relative imports use dots: . = current package, .. = parent")

    # __init__.py
    show(
        "# mypackage/__init__.py\n"
        "# Makes a directory into a Python package\n"
        "# Can be empty, or define package-level exports:\n\n"
        "from mypackage.core import main_function\n"
        "__version__ = '1.0.0'\n"
        "__all__ = ['main_function', '__version__']"
    )
    print("__init__.py runs when the package is imported")
    print("__all__ controls what 'from package import *' exports")

    # __all__
    show(
        "# module.py\n"
        "__all__ = ['public_func', 'PublicClass']\n\n"
        "def public_func(): ...    # exported by import *\n"
        "def _private(): ...       # not exported (convention)\n"
        "class PublicClass: ...    # exported by import *"
    )
    import os

    os_exports = len(os.__all__) if hasattr(os, "__all__") else "not defined"
    print(f"os module __all__ has {os_exports} exports")

    # sys.path
    show("import sys\nsys.path  # list of directories Python searches for modules")
    print(f"sys.path has {len(sys.path)} entries")
    print(f"  first: {sys.path[0]!r}")
    print(f"  last:  {sys.path[-1]!r}")

    # __name__ and __main__
    show(
        "# script.py\n"
        "if __name__ == '__main__':\n"
        "    main()  # only runs when executed directly\n\n"
        "# When imported: __name__ == 'script'\n"
        "# When run:      __name__ == '__main__'"
    )
    print(f"This module's __name__: {__name__!r}")

    # Module attributes
    show(
        "import os\n"
        "os.__name__    # 'os'\n"
        "os.__file__    # path to source file\n"
        "os.__doc__     # module docstring\n"
        "os.__package__ # package name"
    )
    print(f"sys.__name__    = {sys.__name__!r}")
    print(f"sys.__package__ = {sys.__package__!r}")


@example(
    "Modules & Packaging",
    "Packaging: __main__.py, entry points, pyproject.toml structure",
    doc_url="https://packaging.python.org/en/latest/",
)
def packaging_example() -> None:
    """Demonstrate Python packaging concepts and pyproject.toml structure."""
    # __main__.py
    show(
        "# mypackage/__main__.py\n"
        "# Allows: python -m mypackage\n\n"
        "from mypackage.cli import main\n"
        "main()"
    )
    print("python -m mypackage runs mypackage/__main__.py")

    # pyproject.toml structure
    show(
        "# pyproject.toml (modern Python packaging)\n"
        "[project]\n"
        'name = "mypackage"\n'
        'version = "1.0.0"\n'
        'description = "A cool package"\n'
        'requires-python = ">=3.10"\n'
        "dependencies = [\n"
        '    "requests>=2.28",\n'
        '    "click>=8.0",\n'
        "]\n\n"
        "[project.scripts]\n"
        'mycommand = "mypackage.cli:main"    # entry point\n\n'
        "[build-system]\n"
        'requires = ["hatchling"]\n'
        'build-backend = "hatchling.build"'
    )
    print("pyproject.toml replaces setup.py and setup.cfg")
    print("  [project]        — metadata and dependencies")
    print("  [project.scripts] — CLI entry points")
    print("  [build-system]   — build tool configuration")

    # src layout
    show(
        "# Recommended project layout:\n"
        "myproject/\n"
        "  pyproject.toml\n"
        "  README.md\n"
        "  src/\n"
        "    mypackage/\n"
        "      __init__.py\n"
        "      __main__.py    # python -m mypackage\n"
        "      cli.py\n"
        "      core.py\n"
        "  tests/\n"
        "    conftest.py\n"
        "    test_core.py"
    )
    print("src/ layout prevents accidental imports from the working directory")

    # Common tools
    show(
        "# Modern Python toolchain:\n"
        "# uv        — fast dependency management (replaces pip + venv)\n"
        "# ruff      — fast linter and formatter (replaces flake8, black, isort)\n"
        "# ty        — type checker\n"
        "# pytest    — test runner\n"
        "# pre-commit — git hooks for code quality"
    )
    print("Tools: uv (deps), ruff (lint/fmt), pytest (test), pre-commit (hooks)")

    # Building and publishing
    show(
        "# Build and publish:\n"
        "uv build                   # creates dist/*.whl and dist/*.tar.gz\n"
        "uv publish                 # upload to PyPI\n\n"
        "# Install from source:\n"
        "uv pip install -e '.[dev]' # editable install with dev extras"
    )
    print("uv build creates wheel + sdist in dist/")
    print("uv publish uploads to PyPI (needs API token)")
