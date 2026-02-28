# link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # O(n) time and O(1) space
        low -= low % 2
        high += high % 2
        return (high - low) // 2
