# link: https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # O(n log n) time and O(1) space
        costs.sort()
        result = 0
        for c in costs:
            if c > coins:
                break
            result += 1
            coins -= c
        return result
