# link: https://leetcode.com/problems/smallest-number-with-all-set-bits/


class Solution:
    def smallestNumber(self, n: int) -> int:
        # O(n) time and O(1) space
        result = 1
        while result < n:
            result = result * 2 + 1
        return result
