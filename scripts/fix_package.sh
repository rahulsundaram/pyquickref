#!/bin/bash
set -e

# Define colors for pretty output
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print header
echo -e "${BLUE}==============================================${NC}"
echo -e "${BLUE}Fixing PyQuickRef Package Structure${NC}"
echo -e "${BLUE}==============================================${NC}"

# Get the project root directory
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

# Create package directory if it doesn't exist
if [ ! -d "pyquickref" ]; then
    echo -e "\n${YELLOW}Creating pyquickref package directory...${NC}"
    mkdir -p pyquickref

    # Create __init__.py
    echo -e "\"\"\"PyQuickRef - A comprehensive reference for Python functionality with runnable examples.\"\"\"\n\n__version__ = \"0.1.0\"" > pyquickref/__init__.py
    echo -e "${GREEN}Created package directory and __init__.py${NC}"
fi

# Display status message
echo -e "\n${GREEN}Package structure fixed.${NC}"
echo -e "${YELLOW}You can now install the package with:${NC}"
echo -e "  pip install -e ."
echo -e "${YELLOW}Or run the tests with:${NC}"
echo -e "  ./scripts/run_tests.sh"

exit 0
