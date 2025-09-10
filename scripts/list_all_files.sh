#!/bin/bash

# This script lists all files in the current repository that are not ignored by git,
# and prints their contents. It is intended to be used when repository files need to be
# provided within an AI prompt.
# For files matching certain patterns, it prints '[contents skipped]' instead of the content.

# Define patterns for files whose contents should be skipped
SKIP_PATTERNS=(
    "*test_data/*"
    "*workspace/*"
    "*scripts/*"
    "*dependencies_docs/*"
)

# Function to check if a file matches any skip pattern
should_skip_contents() {
    local file_path="$1"
    for pattern in "${SKIP_PATTERNS[@]}"; do
        if [[ "$file_path" == $pattern ]]; then
            return 0  # true - should skip
        fi
    done
    return 1  # false - should not skip
}

# Check if git is installed
if ! command -v git &> /dev/null
then
    echo "git could not be found. Please install git to run this script."
    exit 1
fi

# Check if inside a git repository
if ! git rev-parse --is-inside-work-tree &> /dev/null
then
    echo "Not inside a git repository."
    exit 1
fi

# It is long, but for LLMs it is usually parsed as a single token
SEPARATOR="========================================"

# First, show the project tree structure
echo "$SEPARATOR"
echo "PROJECT TREE"
echo "$SEPARATOR"
tree -I '__pycache__|*.pyc|.git|.pytest_cache|.ruff_cache|*.egg-info|.venv|venv|env|.env' --dirsfirst -L 4
echo "$SEPARATOR"

# Function to process and print file contents
process_file() {
    local file_path="$1"

    # This check is important because ls-files can list files that are staged for deletion but no longer exist on disk.
    if [ ! -f "$file_path" ]; then
        return
    fi

    echo "" # for spacing
    echo "$SEPARATOR"
    echo "FILE: $file_path"
    echo "$SEPARATOR"

    if should_skip_contents "$file_path"; then
        # Get file stats for skipped files
        local file_size=$(stat -f%z "$file_path" 2>/dev/null || stat -c%s "$file_path" 2>/dev/null || echo "unknown")
        local line_count=$(wc -l < "$file_path" 2>/dev/null || echo "unknown")
        echo "[contents skipped - size: $file_size bytes, lines: $line_count]"
    # Check if the file is binary. The `file` command is a good heuristic.
    # The `-b` option prevents printing the filename.
    elif file -b --mime-encoding "$file_path" | grep -q "binary"; then
        # Get file size for binary files
        local file_size=$(stat -f%z "$file_path" 2>/dev/null || stat -c%s "$file_path" 2>/dev/null || echo "unknown")
        echo "[Binary file - contents not shown - size: $file_size bytes]"
    else
        # Check if file is empty, like the python script does.
        if [ -s "$file_path" ]; then
            cat "$file_path"
        else
            echo "[Empty file]"
        fi
    fi
    echo "$SEPARATOR"
}

# First, process README.md if it exists
if [ -f "README.md" ]; then
    process_file "README.md"
fi

# Then process other files from the main directory (excluding README.md)
git ls-files --cached --others --exclude-standard | grep -E "^[^/]+$" | grep -v "^README.md$" | sort | while IFS= read -r file_path; do
    process_file "$file_path"
done

# Finally, process all files in subdirectories
git ls-files --cached --others --exclude-standard | grep "/" | sort | while IFS= read -r file_path; do
    process_file "$file_path"
done
