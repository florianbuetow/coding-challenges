# O(n) time and O(1) space
# link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/


class Solution:
    def minimumDeletions(self, s: str) -> int:
        result = counter = 0
        for c in s:
            if c == 'b':
                counter += 1
            elif counter > 0:
                result += 1
                counter -= 1
        return result
