#!/usr/bin/env python
"""Test runner script for PyQuickRef.

Note: This script is named 'run_tests.py' while the actual test cases are in 'tests.py'.
In a future refactoring, we plan to move all tests to a dedicated 'tests/' directory
and rename this script to something more appropriate like 'test_runner.py'.
"""

import importlib.util
import os
import shutil  # Use shutil.which instead of subprocess for locating executables
import subprocess
import sys
import unittest


def ensure_dependencies() -> None:
    """Make sure dependencies are installed before running tests."""
    # Check if yaml is installed
    if importlib.util.find_spec("yaml") is None:
        print("PyYAML not installed. Installing required dependencies...")
        try:
            # Use shutil.which to locate uv
            uv_path = shutil.which("uv")
            if uv_path:
                subprocess.run(
                    [uv_path, "pip", "install", "pyyaml", "pytest"],
                    check=True,
                )
            else:
                print("uv not found. Please install uv: pip install uv")
                print("See https://github.com/astral-sh/uv for more information.")
                sys.exit(1)
            print("Dependencies installed successfully.")
        except subprocess.SubprocessError:
            print("Failed to install dependencies. Please run:")
            print("uv pip install pyyaml pytest")
            sys.exit(1)


def run_tests() -> int:
    """Run all the tests for PyQuickRef.

    Returns
    -------
        int: 0 if all tests passed, 1 if any tests failed

    """
    # Ensure dependencies are installed
    ensure_dependencies()

    # Add the parent directory to sys.path to ensure imports work
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(script_dir)

    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = script_dir
    suite = loader.discover(start_dir, pattern="tests.py")

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Return non-zero exit code if tests failed
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
