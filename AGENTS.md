# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains Python solutions to coding challenges from LeetCode, Deep-ML, Codewars, and Advent of Code platforms. Solutions are organized by platform and difficulty, and the README.md is auto-generated from solution file metadata.

## Key Commands

### Generate README

**CRITICAL:** ALWAYS use `make generate` to regenerate the README. NEVER run `python3 generate_readme.py` directly or use any other method.

```bash
make generate   # ALWAYS use this to generate README
```

**If `make generate` fails because Docker is not running:**
- **STOP immediately** and report the error to the user
- **DO NOT** attempt to run `python3 generate_readme.py` as a fallback
- **DO NOT** try alternative methods
- The user must start Docker before proceeding

**Makefile targets:**
- `make help` - Show available targets (default)
- `make init` - Build Docker image (run this first, or after modifying generate_readme.py)
- `make generate` - Generate README using existing Docker image (ALWAYS USE THIS)
- `make status` - Check if Docker image exists
- `make destroy` - Delete Docker image

The `init` target uses `--no-cache` to prevent stale code issues.

**IMPORTANT:** The `generate_readme.py` script is copied into the Docker image at build time. After modifying `generate_readme.py`, you MUST run `make destroy && make init` to rebuild the Docker image before running `make generate`.

## Architecture

### README Generation System

The repository uses an automated documentation system:

1. **generate_readme.py** - Core script that:
   - Walks through `platform/difficulty/` directory structure (2 levels deep)
   - Parses each `.py` file for complexity annotations and problem links
   - Extracts problem numbers from filenames
   - Generates markdown tables sorted numerically by problem number
   - Injects content from `DESCRIPTION.md` and `USAGE.md`

2. **Docker Build** - `generate_readme_using_docker.sh` and `Dockerfile` create a Python 3.11 container that runs the generator and persists output to the host.

### Directory Structure
```
leetcode/
  ├── easy/
  ├── medium/
  └── hard/
deep-ml/
  ├── easy/
  └── medium/
codewars/
  ├── kyu-4/
  ├── kyu-5/
  └── ...
aoc/
  └── {year}/
      └── day-{XX}/
          ├── problem.txt
          ├── input_0.txt
          ├── input_1.txt
          ├── solution_part_1.py
          └── solution_part_2.py
```

## Solution File Format (Critical)

Every solution file MUST follow this format for the parser to extract metadata correctly:

### Complexity Annotations

Add a comment with complexity information near the top of the file:

```python
# O(n) time and O(1) space
```

**Supported patterns:**
- `# O(n) time and O(1) space` - Standard format
- `# O(1) space and O(n) time` - Reversed order (parser handles this)
- `# O(n) time and space` - Same complexity for both
- `# O(n) time` - Time only (space will be "N/A")
- `# O(1) space` - Space only (time will be "N/A")

**Parser behavior:**
- Only searches comment lines (starting with `#`)
- Case-insensitive keyword matching for `time` and `space`
- Stops after finding BOTH time AND space complexity
- Returns "N/A" if not found
- First match wins - you cannot override later in the file

### Problem Link Annotation

```python
# link: https://leetcode.com/problems/problem-name/
```

Or use `source:` instead of `link:` (case-insensitive). The parser extracts the first URL found.

### File Naming Convention

Format: `{number}{separator}{Problem Name}.py`

Examples:
- `3110. Score of a String.py` → Problem #3110
- `1 Matrix times Vector.py` → Problem #1
- `Calculate 2x2 Matrix Inverse.py` → No number, uses array index

The parser extracts the leading number and removes it (plus following non-whitespace) from the display name. Problems are sorted numerically.

## Adding a New Solution

**CRITICAL WORKFLOW - Follow these steps EXACTLY:**
1. Create the solution file with proper format (complexity annotation + link)
2. Commit the solution file first (CHANGES.md reads git log, so solution must be committed first)
3. Run `make generate`
4. Commit README.md and CHANGES.md
5. Push to remote

**NEVER skip any steps. The order matters because CHANGES.md is generated from git history.**

### LeetCode / Deep-ML

1. Create file in appropriate directory: `{platform}/{difficulty}/{number}. {Problem Name}.py`
2. Add complexity annotation in comments (exactly one blank line before the class):
   ```python
   # O(n) time and O(1) space
   # link: https://leetcode.com/problems/problem-name/

   class Solution:
   ```
3. Implement the solution
4. Commit the solution file
5. Run `make generate`
6. Commit README.md + CHANGES.md, then push

### Codewars

1. Create file: `codewars/kyu-{level}/{problem_name}.py` (snake_case, no number prefix)
2. Add annotations:
   ```python
   # O(n) time and space
   # Link: https://www.codewars.com/kata/{kata_id}

   class Solution:
   ```
3. Commit the solution file
4. Run `make generate`
5. Commit README.md + CHANGES.md, then push

### Advent of Code

1. Create directory: `aoc/{year}/day-{XX}/` (XX is zero-padded day number)
2. Add files:
   - `problem.txt` - First line must be `--- Day X: Challenge Name ---`
   - `input_0.txt` - Sample input
   - `input_1.txt` - Puzzle input
   - `solution_part_1.py` and `solution_part_2.py`
3. Add annotations in solution files:
   ```python
   # O(n) time and O(1) space
   # link: https://adventofcode.com/{year}/day/{day}

   class Solution:
   ```
4. Empty solution files are automatically skipped in README generation
5. Commit the solution files
6. Run `make generate`
7. Commit README.md + CHANGES.md, then push

## Important Notes

- **Never edit README.md manually** - it's auto-generated and changes will be overwritten
- To modify README content, edit `DESCRIPTION.md` or `USAGE.md` instead
- **README.md structure**:
  - DESCRIPTION.md content is inserted at the top
  - Problem tables are auto-generated from solution files
  - USAGE.md content is appended at the end
- Only `.py` files are processed by the generator
- The parser uses only Python stdlib (os, re, urllib.parse) - no external dependencies
- File paths in README are URL-encoded to handle spaces and special characters

## Git Commit Guidelines

**IMPORTANT:** When creating git commits in this repository:
- **NEVER** include Claude Code attribution in commit messages
- **NEVER** add "Generated with Claude Code" or similar phrases
- **NEVER** add "Co-Authored-By: Claude" or similar attribution
- **NEVER** run `git add -A` or `git add .` - always stage files explicitly
- **Separate commits for infrastructure files** - Always commit changes to CLAUDE.md, Makefile, and USAGE.md independently from changes to files in subfolders (leetcode, deep-ml, etc.). Make separate commits for infrastructure/documentation changes vs solution changes
- **Commit message format** - Use a single sentence (max two sentences). Use `git status` to understand what changed before writing the commit message
- **Keep commit messages professional** and focused on the changes made
- **Commit messages should describe what changed and why**, without mentioning AI assistance
- **When adding new solutions** - Use simple format like "Add LC {number} ({difficulty})" - do NOT add "and update documentation" (README regeneration is implied), and do NOT add complexity details, algorithm descriptions, or implementation notes in commit messages
- **ALWAYS push commits to remote after committing** - run `git push` after successful `git commit`
