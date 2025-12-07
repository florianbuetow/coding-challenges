# O(1) time and space
# link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low -= low % 2
        high += high % 2
        return (high - low) // 2
