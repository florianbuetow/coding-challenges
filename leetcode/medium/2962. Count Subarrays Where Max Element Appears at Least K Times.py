from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
        result, left, counter, m = 0, 0, 0, max(nums)
        for right, n in enumerate(nums):
            if n == m:
                counter += 1
            while counter == k:
                if nums[left] == m:
                    counter -= 1
                left += 1
            result += left
        return result