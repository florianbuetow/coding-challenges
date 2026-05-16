# link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        return min(nums)
