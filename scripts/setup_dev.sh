#!/bin/bash
set -e

# Define colors for pretty output
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}==============================================${NC}"
echo -e "${BLUE}Setting Up Development Environment for PyQuickRef${NC}"
echo -e "${BLUE}==============================================${NC}"

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo -e "${RED}Python is not installed. Please install Python 3.9+ and try again.${NC}"
    exit 1
fi

# Check if uv is installed, install if not
if ! command -v uv &> /dev/null; then
    echo -e "\n${YELLOW}uv is not installed. Installing uv...${NC}"
    if pip install uv; then
        echo -e "${GREEN}uv installed successfully.${NC}"
    else
        echo -e "${RED}Failed to install uv. Please install it manually with: pip install uv${NC}"
        echo -e "${RED}Then run this script again.${NC}"
        exit 1
    fi
fi

# Make run_tests.sh executable
echo -e "\n${YELLOW}Making scripts executable...${NC}"
if chmod +x "$(dirname "$0")/run_tests.sh"; then
    if chmod +x "$0"; then
        echo -e "${GREEN}Scripts are now executable.${NC}"
    else
        echo -e "${RED}Failed to make setup_dev.sh executable.${NC}"
        exit 1
    fi
else
    echo -e "${RED}Failed to make run_tests.sh executable.${NC}"
    exit 1
fi

# Install dependencies
echo -e "\n${YELLOW}Installing dependencies...${NC}"
if uv pip install -e ".[dev]"; then
    echo -e "${GREEN}Dependencies installed successfully with uv.${NC}"
else
    echo -e "${RED}Failed to install dependencies with uv.${NC}"
    exit 1
fi

# Install pytest
echo -e "\n${YELLOW}Ensuring pytest is installed...${NC}"
if uv pip install pytest; then
    echo -e "${GREEN}pytest installed successfully.${NC}"
else
    echo -e "${RED}Failed to install pytest. Some tests may not run correctly.${NC}"
fi

# Install pre-commit
echo -e "\n${YELLOW}Installing pre-commit hooks...${NC}"
if ! command -v pre-commit &> /dev/null; then
    echo "Installing pre-commit with uv..."
    if uv pip install pre-commit; then
        echo -e "${GREEN}Pre-commit installed successfully.${NC}"
    else
        echo -e "${RED}Failed to install pre-commit.${NC}"
        exit 1
    fi
fi

if pre-commit install; then
    echo -e "${GREEN}Pre-commit hooks installed successfully.${NC}"
else
    echo -e "${RED}Failed to install pre-commit hooks.${NC}"
    exit 1
fi

echo -e "\n${GREEN}=== Development environment setup complete! ===${NC}"
echo -e "${YELLOW}You can now run tests using:${NC}"
echo -e "  ./scripts/run_tests.sh"
echo -e "${YELLOW}Or run individual test components with:${NC}"
echo -e "  uv run pytest             # Run unit tests"
echo -e "  uv run mypy .             # Run type checking"
echo -e "  uv run ruff check .       # Run linting"
echo -e "  uv run ruff format .      # Run code formatting"
echo -e "${YELLOW}Before committing, tests will automatically run via pre-commit hook.${NC}"
exit 0
