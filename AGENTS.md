# CLAUDE.md

- Do not preserve backward compatibility.
- Choose the simplest implementation that fully meets the current requirements.
- Prefer established, well-maintained libraries over custom implementations.

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains Python solutions to coding challenges from LeetCode, Deep-ML, Codewars, and Advent of Code. Solutions are organized by platform and difficulty. README.md and CHANGES.md are auto-generated.

## Just Commands

| Command | Description |
|---------|-------------|
| `just generate` | Generate README.md and CHANGES.md |
| `just ci` | Run CI checks (semgrep) |
| `just destroy` | Remove virtual environment |

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
| `generate_readme.py` | README generator script |
