"""Command-line interface for PyQuickRef.

This module provides the command-line interface for running PyQuickRef.
"""

import argparse
from typing import Optional

import yaml

from pyquickref.core import PyQuickRef
from pyquickref.utils.logging import setup_logger


def parse_args() -> argparse.Namespace:
    """Parse command line arguments.

    Returns
    -------
        Parsed arguments

    """
    parser = argparse.ArgumentParser(description="Python Quick Reference Examples")
    parser.add_argument("--functions", nargs="+", help="Specific functions to run")
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL", "NONE"],
        default="INFO",
        help="Set logging level",
    )
    parser.add_argument("--quiet", action="store_true", help="Suppress console output")
    parser.add_argument("--log-file", help="Log to specified file")
    parser.add_argument("--config", help="Path to YAML config file")
    parser.add_argument(
        "--output-dir",
        default="data",  # Updated default directory
        help="Directory for file outputs (default: data)",
    )

    return parser.parse_args()


def main() -> None:
    """Run the main entry point of the PyQuickRef application.

    Parses command-line arguments, configures logging, initializes the PyQuickRef class,
    and executes the specified functions.
    """
    args = parse_args()

    # Set up logging
    logger = setup_logger(
        level="NONE" if args.quiet else args.log_level,
        quiet=args.quiet,
        log_file=args.log_file,
    )

    # Create PyQuickRef instance
    pyquickref = PyQuickRef(logger, args.output_dir)

    # Determine functions to run
    functions_to_run: Optional[list[str]] = None

    # If config file is provided, try to load functions from it
    if args.config:
        try:
            with open(args.config) as config_file:
                config = yaml.safe_load(config_file)
                if "functions" in config:
                    functions_to_run = config["functions"]
        except Exception as e:
            logger.error(f"Error loading config file: {e}")

    # Command line arguments override config file
    if args.functions:
        functions_to_run = args.functions

    # Run the specified examples
    pyquickref.run_examples(functions_to_run)


if __name__ == "__main__":
    main()
