# O(n log n) time and O(1) space
# link: https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_window = 0
        left = right = 0
        while right < len(nums):
            if nums[right] > nums[left] * k:
                left += 1
                continue
            cur_window = abs(right - left + 1)
            max_window = max(max_window, cur_window)
            right += 1
        return len(nums) - max_window
