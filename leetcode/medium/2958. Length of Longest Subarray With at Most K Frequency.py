# link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # O(n) time and space
        result = left = 0
        window = defaultdict(int)
        for right, curr in enumerate(nums):
            window[curr] += 1
            while window[curr] > k:
                prev = nums[left]
                window[prev] -= 1
                left += 1
            window_size = right - left + 1
            result = max(result, window_size)
        return result
