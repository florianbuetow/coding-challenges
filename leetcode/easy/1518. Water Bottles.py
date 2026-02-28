# link: https://leetcode.com/problems/water-bottles/


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # O(n) time and O(1) space
        return numBottles + (numBottles - 1) // (numExchange - 1)
