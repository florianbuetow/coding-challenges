---
name: adding-solution
description: Use when adding a new LeetCode, Deep-ML, Codewars, or Advent of Code solution.
user-invocable: false
metadata:
  internal: true
---

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

**LeetCode files** must follow this exact structure (enforced by semgrep CI):

```python
# link: https://leetcode.com/problems/problem-name/

class Solution:
    def methodName(self, ...) -> ...:
        # O(n) time and O(1) space
        ...
```

Rules:
1. **First line** must be `# link: https://leetcode.com/problems/...`
2. **Second line** must be blank
3. **Complexity comment** must be the first line inside the method (not at file level)
4. Do NOT put the complexity comment both at file level and inside the method

**Other platforms** (Deep-ML, Codewars, AoC) use file-level complexity comments:

```python
# O(n) time and O(1) space
# link: https://...

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

**NEVER** modify the user's complexity annotations. If you believe an annotation is incorrect, ask the user about it instead of changing it.
