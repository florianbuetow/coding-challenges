# link: https://leetcode.com/problems/water-bottles-ii/


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # O(n) time and O(1) space
        result = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            emptyBottles = emptyBottles - numExchange + 1
            numExchange += 1
            result += 1
        return result
