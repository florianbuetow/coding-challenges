from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) space and time
        # link: https://leetcode.com/problems/product-of-array-except-self/
        # idea: two passes over nums using prefix product and postfix product
        result = [1] * len(nums)

        product = 1 # this is our prefix product
        for i in range(len(nums)):
            result[i] *= product
            product *= nums[i]

        product = 1 # this is our postfix product
        for i in range(len(nums)-1,-1,-1):
            result[i] *= product
            product *= nums[i]

        return result