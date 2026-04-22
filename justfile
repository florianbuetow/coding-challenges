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
#    - On success: green (\033[0;32m) message confirming completion.
#      E.g. printf "\033[0;32m✓ init completed successfully\033[0m\n"
#    - On failure: red (\033[0;31m) message indicating what failed, then exit 1.
#      E.g. printf "\033[0;31m✗ ci failed: tests exited with errors\033[0m\n"
# =============================================================================

# Default recipe: show available commands
_default:
    @just help

# Show available targets
help:
    @echo ""
    @clear
    @echo ""
    @printf "\033[0;34m=== coding-challenges ===\033[0m\n"
    @echo ""
    @printf "\033[0;33mSolutions:\033[0m\n"
    @printf "  %-38s %s\n" "generate" "Generate README.md and CHANGES.md"
    @printf "  %-38s %s\n" "graph" "Generate solutions growth chart"
    @printf "  %-38s %s\n" "leetcode" "Show last 10 accepted LeetCode submissions"
    @echo ""
    @printf "\033[0;33mCode Quality:\033[0m\n"
    @printf "  %-38s %s\n" "ci" "Run CI checks (semgrep)"
    @echo ""
    @printf "\033[0;33mLifecycle:\033[0m\n"
    @printf "  %-38s %s\n" "destroy" "Remove virtual environment"
    @echo ""

# Generate README.md and CHANGES.md
generate: graph
    #!/usr/bin/env bash
    echo ""
    if uv run generate_readme.py; then
        printf "\033[0;32m✓ README.md and CHANGES.md generated successfully\033[0m\n"
    else
        printf "\033[0;31m✗ generate failed: uv run exited with errors\033[0m\n"
        exit 1
    fi
    echo ""

# Generate solutions growth chart
graph:
    #!/usr/bin/env bash
    echo ""
    if uv run generate_graph.py; then
        git add solutions_growth.png
        printf "\033[0;32m✓ solutions growth chart generated successfully\033[0m\n"
    else
        printf "\033[0;31m✗ graph failed: uv run exited with errors\033[0m\n"
        exit 1
    fi
    echo ""

# Show last 10 accepted LeetCode submissions for sudoplz
leetcode:
    #!/usr/bin/env bash
    echo ""
    uv run leetcode_recent.py || exit 1
    printf "\033[0;32m✓ done\033[0m\n"
    echo ""

# Run CI checks
ci:
    #!/usr/bin/env bash
    echo ""
    output=$(semgrep --error --config .semgrep.yml leetcode/ 2>&1)
    if [ $? -eq 0 ]; then
        printf "\033[0;32m✓ ci passed\033[0m\n"
    else
        echo "$output" | grep -B2 -A5 "❯❯❱" | head -8
        echo ""
        printf "\033[0;31m✗ ci failed: semgrep found violations (showing first)\033[0m\n"
        echo ""
        exit 1
    fi
    echo ""

# Remove virtual environment
destroy:
    #!/usr/bin/env bash
    echo ""
    if [ -d .venv ]; then
        rm -rf .venv
        printf "\033[0;32m✓ Virtual environment removed\033[0m\n"
    else
        printf "\033[0;32m✓ No virtual environment to remove\033[0m\n"
    fi
    echo ""
