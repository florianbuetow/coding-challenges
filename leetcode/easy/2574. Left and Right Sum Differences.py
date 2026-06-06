# link: https://leetcode.com/problems/left-and-right-sum-differences/


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # O(n) time and space
        result = [0] * len(nums)
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            result[i] = abs(left_sum - right_sum)
            left_sum += nums[i]
        return result
