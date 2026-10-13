# link: https://leetcode.com/problems/maximum-alternating-sum-of-squares

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # O(n log n) time and O(1) space
        result = 0
        nums.sort(key=abs)
        negative_count = len(nums) // 2
        for i, val in enumerate(nums):
            if i < negative_count:
                result -= val ** 2
            else:
                result += val ** 2
        return result
