#!/bin/bash
set -e

# Define colors for pretty output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print header
echo -e "${BLUE}==============================================${NC}"
echo -e "${BLUE}Running Tests for PyQuickRef${NC}"
echo -e "${BLUE}==============================================${NC}"

# Ensure dependencies are installed
echo -e "\n${YELLOW}Checking and installing dependencies...${NC}"
if command -v uv &> /dev/null; then
    echo "Using uv to install dependencies..."
    if uv pip install -e ".[dev]"; then
        echo -e "${GREEN}Dependencies installed successfully.${NC}"
    else
        echo -e "${RED}Failed to install dependencies with uv${NC}"
        exit 1
    fi
else
    echo "uv not found, please install it with: pip install uv"
    echo "See https://github.com/astral-sh/uv for more information."
    exit 1
fi

# Run type checking with mypy
echo -e "\n${YELLOW}Running type checking with mypy...${NC}"
if uv run mypy .; then
    echo -e "${GREEN}Type checking passed!${NC}"
else
    echo -e "${RED}Type checking failed!${NC}"
    exit 1
fi

# Run code formatting check with ruff
echo -e "\n${YELLOW}Checking code formatting with ruff...${NC}"
if uv run ruff format --check .; then
    echo -e "${GREEN}Code formatting check passed!${NC}"
else
    echo -e "${RED}Code formatting check failed!${NC}"
    exit 1
fi

# Run linting with ruff
echo -e "\n${YELLOW}Linting code with ruff...${NC}"
if uv run ruff check .; then
    echo -e "${GREEN}Linting passed!${NC}"
else
    echo -e "${RED}Linting failed!${NC}"
    exit 1
fi

# Run unit tests with pytest directly
echo -e "\n${YELLOW}Running unit tests with pytest...${NC}"
if uv run pytest; then
    echo -e "${GREEN}All tests passed!${NC}"
else
    echo -e "${RED}Tests failed!${NC}"
    exit 1
fi

echo -e "\n${GREEN}=== All checks passed successfully! ===${NC}"
exit 0
