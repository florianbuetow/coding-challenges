# link: https://leetcode.com/problems/maximum-total-subarray-value-i/


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # O(n) time and O(1) space
        return k * (max(nums) - min(nums))
