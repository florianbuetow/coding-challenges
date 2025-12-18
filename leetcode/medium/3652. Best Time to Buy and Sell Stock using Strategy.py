# O(n) time and O(1) space
# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        result = old = new = 0
        for i in range(k):
            old += prices[i] * strategy[i]
        for i in range(k // 2, k):
            new += prices[i]
        result = max(result, new - old)
        for right in range(k, len(prices)):
            left = right - k + 1
            old += prices[right] * strategy[right] - prices[left - 1] * strategy[left - 1]
            new += prices[right] - prices[left - 1 + k // 2]
            result = max(result, new - old)
        for i in range(len(prices)):
            result += prices[i] * strategy[i]
        return result
