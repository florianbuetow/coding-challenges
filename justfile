# =============================================================================
# Justfile Rules (follow these when editing justfile):
#
# 1. Use printf (not echo) to print colors — some terminals won't render
#    colors with echo.
#
# 2. Always add an empty `@echo ""` line before and after each target's
#    command block.
#
# 3. Always add new targets to the help section and update it when targets
#    are added, modified or removed.
#
# 4. Target ordering in help (and in this file) matters:
#    - Setup targets first (init, setup, install, etc.)
#    - Start/stop/run targets next
#    - Code generation / data tooling targets next
#    - Checks, linting, and tests next (ordered fastest to slowest)
#    Group related targets together and separate groups with an empty
#    `@echo ""` line in the help output.
#
# 5. Composite targets (e.g. ci) that call multiple sub-targets must fail
#    fast: exit 1 on the first error. Never skip over errors or warnings.
#    Use `set -e` or `&&` chaining to ensure immediate abort with the
#    appropriate error message.
#
# 6. Every target must end with a clear short status message:
#    - On success: green (\033[32m) message confirming completion.
#      E.g. printf "\033[32m✓ init completed successfully\033[0m\n"
#    - On failure: red (\033[31m) message indicating what failed, then exit 1.
#      E.g. printf "\033[31m✗ ci failed: tests exited with errors\033[0m\n"
# =============================================================================

# Default target
default: help

# Show available targets
help:
    @echo ""
    @printf "\033[1mAvailable targets:\033[0m\n"
    @echo ""
    @printf "  \033[36minit\033[0m       Build Docker image for README generation\n"
    @printf "  \033[36mgenerate\033[0m   Generate README.md and CHANGES.md\n"
    @printf "  \033[36mci\033[0m         Run CI checks (semgrep)\n"
    @printf "  \033[36mdestroy\033[0m    Remove Docker image\n"
    @printf "  \033[36mstatus\033[0m     Check if Docker image exists\n"
    @echo ""

# Build Docker image if it doesn't exist
init:
    #!/usr/bin/env bash
    echo ""
    if docker image inspect readme-generator >/dev/null 2>&1; then
        printf "\033[32m✓ Docker image already exists\033[0m\n"
    elif docker build --no-cache -t readme-generator .; then
        printf "\033[32m✓ init completed successfully\033[0m\n"
    else
        printf "\033[31m✗ init failed: docker build exited with errors\033[0m\n"
        exit 1
    fi
    echo ""

# Generate README.md and CHANGES.md using Docker
generate: init
    #!/usr/bin/env bash
    echo ""
    if docker run --rm \
        -v "$(pwd)":/app \
        -w /app \
        readme-generator; then
        printf "\033[32m✓ README.md and CHANGES.md generated successfully\033[0m\n"
    else
        printf "\033[31m✗ generate failed: docker run exited with errors\033[0m\n"
        exit 1
    fi
    echo ""

# Run CI checks
ci:
    #!/usr/bin/env bash
    echo ""
    output=$(semgrep --error --config .semgrep.yml leetcode/ 2>&1)
    if [ $? -eq 0 ]; then
        printf "\033[32m✓ ci passed\033[0m\n"
    else
        echo "$output" | grep -A5 "❯❯❱" | head -8
        echo ""
        printf "\033[31m✗ ci failed: semgrep found violations (showing first)\033[0m\n"
        echo ""
        exit 1
    fi
    echo ""

# Remove Docker image
destroy:
    #!/usr/bin/env bash
    echo ""
    if docker rmi -f readme-generator:latest; then
        printf "\033[32m✓ Docker image removed\033[0m\n"
    else
        printf "\033[31m✗ destroy failed: docker rmi exited with errors\033[0m\n"
        exit 1
    fi
    echo ""

# Check if Docker image exists
status:
    @echo ""
    @if docker image inspect readme-generator >/dev/null 2>&1; then \
        printf "\033[32m✓ Docker image exists. Run 'just generate' to generate README.md\033[0m\n"; \
    else \
        printf "\033[33m⚠ Docker image does not exist. Run 'just init' to create it.\033[0m\n"; \
    fi
    @echo ""
