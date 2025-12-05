# O(n) time and O(1) space
# link: https://leetcode.com/problems/count-partitions-with-even-sum-difference/

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        result = 0
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum % 2 == right_sum % 2:
                result += 1
        return result
