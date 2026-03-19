# link: https://leetcode.com/problems/count-commas-in-range/

class Solution:
    def countCommas(self, n: int) -> int:
        # O(1) time and space
        return max(0, n - 1000 + 1)
