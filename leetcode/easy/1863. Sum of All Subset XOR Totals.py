# link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        @cache
        def helper(i, value):
            if i >= len(nums): 
                return value
            return helper(i+1, value ^ nums[i]) + helper(i+1, value)
        return helper(0, 0)