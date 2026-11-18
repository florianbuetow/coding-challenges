# link: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution:
    def minChanges(self, s: str) -> int:
        # O(n) time and O(1) space
        result = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                result += 1
        return result
