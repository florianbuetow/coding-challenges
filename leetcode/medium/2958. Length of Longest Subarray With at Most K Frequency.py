from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # O(n) time and space
        # link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
        result = 0
        counter = {}
        left = 0
        for right, n in enumerate(nums):
            counter[n] = counter.get(n, 0) + 1
            while counter[n] > k and left <= right:
                counter[nums[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result