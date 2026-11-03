# link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        return max(nums) * len(nums) - sum(nums)
