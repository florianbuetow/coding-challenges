# O(n) time and O(1) space
# link: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if not prices: return 0
        result = curr = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                curr += 1
            else:
                curr = 1
            result += curr
        return result
