# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains Python solutions to coding challenges from LeetCode, Deep-ML, Codewars, and Advent of Code. Solutions are organized by platform and difficulty. README.md and CHANGES.md are auto-generated.

## Adding a New Solution

**Follow these steps EXACTLY in order:**

1. Create the solution file (see format below)
2. Commit the solution file
3. Run `just generate`
4. Commit README.md + CHANGES.md
5. Push

**The order matters: CHANGES.md is generated from git history, so the solution must be committed before running `just generate`.**

**IMPORTANT:** Do NOT stage README.md or CHANGES.md before running `just generate`. If these files are already staged, the generated output will overwrite the working directory copies but the staged versions will be stale. Always run `just generate` with a clean staging area, then stage and commit the freshly generated files.

### Solution File Format

```python
# O(n) time and O(1) space
# link: https://leetcode.com/problems/problem-name/

class Solution:
    ...
```

### Platform-Specific Details

| Platform | Path | Filename |
|----------|------|----------|
| LeetCode | `leetcode/{easy,medium,hard}/` | `{number}. {Problem Name}.py` |
| Deep-ML | `deep-ml/{easy,medium}/` | `{number} {Problem Name}.py` |
| Codewars | `codewars/kyu-{N}/` | `{problem_name}.py` (snake_case) |
| AoC | `aoc/{year}/day-{XX}/` | `solution_part_1.py`, `solution_part_2.py` |

**Advent of Code** also requires:
- `problem.txt` - First line: `--- Day X: Challenge Name ---`
- `input_0.txt` - Sample input
- `input_1.txt` - Puzzle input

### Complexity Annotation Patterns

- `# O(n) time and O(1) space` - Standard
- `# O(n) time and space` - Same for both
- `# O(n) time` or `# O(1) space` - One only (other shows "N/A")

## Just Commands

| Command | Description |
|---------|-------------|
| `just generate` | Generate README.md and CHANGES.md (ALWAYS use this) |
| `just init` | Build Docker image |
| `just destroy` | Delete Docker image |
| `just status` | Check if Docker image exists |

**If `just generate` fails because Docker is not running:** STOP and tell the user to start Docker. Do NOT run Python scripts directly.

## Modifying Generator Scripts

When editing `generate_readme.py` or `generate_changes.py`:

1. Make your changes to the script
2. Run `just destroy && just init` to rebuild the Docker image
3. Run `just generate` to test
4. Commit the script changes, then commit README.md + CHANGES.md

**The scripts are copied into the Docker image at build time.** If you skip the rebuild, your changes won't take effect.

## Git Guidelines

- **NEVER** include AI attribution in commits
- **NEVER** use `git add -A` or `git add .` - stage files explicitly
- **NEVER** use `git -C` - run git commands directly from the working directory
- **ONLY push at the end** of a workflow (e.g., step 5 of "Adding a New Solution"), not after each commit
- **Commit messages:** Before committing solution files, run `git log --oneline -10` to find similar commits and match their format exactly
- **Separate commits:** Infrastructure changes (AGENTS.md, Makefile, USAGE.md) go in separate commits from solution files

## File Reference

| File | Purpose |
|------|---------|
| `README.md` | Auto-generated, never edit manually |
| `CHANGES.md` | Auto-generated recent changes from git history |
| `DESCRIPTION.md` | Edit this to change README header content |
| `USAGE.md` | Edit this to change README footer content |
| `generate_readme.py` | README generator script (runs in Docker) |
