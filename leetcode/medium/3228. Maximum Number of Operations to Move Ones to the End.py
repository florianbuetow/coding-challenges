# O(n) time and O(1) space
# link: https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end

class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        ones = 0
        gap = False
        for c in s:
            if c == '1':
                if gap:
                    result += ones
                    gap = False
                ones += 1
            else:
                gap = True
        if gap:
            result += ones
        return result
