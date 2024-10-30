from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # O(n log n) time and O(1) space
        # link: https://leetcode.com/problems/largest-unique-number/
        # idea: sort numbers in ascending order, then remove largest until it is unique
        nums.append(-1)
        nums.sort() # O(n log n)
        prev_largest = None
        while len(nums) > 1 and (nums[-1] == nums[-2] or nums[-1] == prev_largest): # O(n)
            prev_largest = nums.pop()
        return nums[-1]

