# link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # O(n log n) time and O(1) space
        result = 0
        nums.sort()
        middle = len(nums) // 2
        median = nums[middle]
        for n in nums:
            result += abs(n - median)
        return result
