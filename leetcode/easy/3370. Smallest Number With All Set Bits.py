# O(log n) time and O(1) space
# link: https://leetcode.com/problems/smallest-number-with-all-set-bits/

class Solution:
    def smallestNumber(self, n: int) -> int:
        result = 1
        while result < n:
            result = result * 2 + 1
        return result
