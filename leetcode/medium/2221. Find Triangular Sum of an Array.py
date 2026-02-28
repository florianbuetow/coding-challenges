# link: https://leetcode.com/problems/find-triangular-sum-of-an-array/


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        while len(nums) > 1:
            newNums = []
            for i in range(0, len(nums) - 1):
                newNums.append((nums[i] + nums[i+1]) % 10)
            nums = newNums
        return nums[0]
