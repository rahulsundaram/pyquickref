"""Logging utilities for PyQuickRef.

This module provides utilities for setting up and configuring logging.
"""

import logging
import sys
from logging import FileHandler
from typing import Optional, cast


def setup_logger(
    level: str = "INFO", quiet: bool = False, log_file: Optional[str] = None
) -> logging.Logger:
    """Set up and configure a logger.

    Args:
    ----
        level: The logging level to use (DEBUG, INFO, WARNING, ERROR, CRITICAL, NONE)
        quiet: Whether to suppress console output
        log_file: Optional file to log to

    Returns:
    -------
        A configured logger instance

    """
    logger = logging.getLogger("pyquickref")

    # Clear any existing handlers
    logger.handlers = []

    if level == "NONE":
        logger.setLevel(logging.CRITICAL)
        logger.addHandler(logging.NullHandler())
        return logger

    # Set the logging level
    logger.setLevel(getattr(logging, level))

    # Create a simple formatter
    formatter = logging.Formatter("%(message)s")

    # Add console handler if not quiet
    if not quiet:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(cast(FileHandler, console_handler))

    # Add file handler if log file specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
