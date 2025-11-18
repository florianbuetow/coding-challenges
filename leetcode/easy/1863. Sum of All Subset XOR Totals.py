# O(n^2) time and O(n) space
# link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        @cache
        def helper(i, value):
            if i >= len(nums): 
                return value
            return helper(i+1, value ^ nums[i]) + helper(i+1, value)
        return helper(0, 0)