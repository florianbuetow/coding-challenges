# O(n) time and O(k) space
# link: https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        result = -float('inf')
        minimum = [float('inf')] * k
        minimum[-1] = 0
        prefix_sum = 0
        for i, n in enumerate(nums):
            prefix_sum += n
            result = max(prefix_sum - minimum[i % k], result)
            minimum[i % k] = min(prefix_sum, minimum[i % k])
        return result
