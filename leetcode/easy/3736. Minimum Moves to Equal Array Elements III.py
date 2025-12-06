# O(n) time and O(1) space
# link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        result = 0
        max_n = max(nums)
        for n in nums:
            result += max_n - n
        return result
