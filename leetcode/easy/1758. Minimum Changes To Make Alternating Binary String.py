# link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        # O(n) time and O(1) space
        errors = [0, 0]
        for i, c in enumerate(s):
            c = int(c)
            errors[0] += [0, 1][c == (i + 0) % 2]
            errors[1] += [0, 1][c == (i + 1) % 2]
        return min(errors)
