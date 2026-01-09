# O(n log n) time and O(1) space
# link: https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum_small = sum_large = 0
        left, right = 0, len(nums) - 1
        for _ in range(k):
            sum_small += nums[left]
            sum_large += nums[right]
            left += 1
            right -= 1
        return abs(sum_large - sum_small)
