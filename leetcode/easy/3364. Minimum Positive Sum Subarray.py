# link: https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # O(n*m) time and O(1) space, n = len(nums)
        result = float('inf')
        for window_size in range(l, r + 1):
            window_sum = 0
            for right in range(len(nums)):
                left = right - window_size + 1
                window_sum += nums[right]
                if left >= 0:
                    if window_sum > 0:
                        result = min(result, window_sum)
                    window_sum -= nums[left]
        if result == float('inf'):
            return -1
        return result
