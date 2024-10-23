class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:        
        # O(n^2) time and O(n) space
        @cache
        def helper(i, value):
            if i >= len(nums): 
                return value
            return helper(i+1, value ^ nums[i]) + helper(i+1, value)
        return helper(0, 0)