# link: https://leetcode.com/problems/water-bottles/


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # O(n) time and O(1) space
        result = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            fullBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange
            result += fullBottles
            emptyBottles += fullBottles
        return result
