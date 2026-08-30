# link: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        min_pos = max_pos = 0
        for cur_pos, n in enumerate(nums):
            if nums[min_pos] > n: min_pos = cur_pos
            if nums[max_pos] < n: max_pos = cur_pos
        left, right = sorted([min_pos + 1, max_pos + 1])
        return min(
            right,
            len(nums) - left + 1,
            left + len(nums) - right + 1
        )
