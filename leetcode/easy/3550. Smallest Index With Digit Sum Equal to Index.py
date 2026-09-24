# link: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # O(n log m) time and O(1) space, n = len(nums), m = max(nums)
        def digitSum(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res

        for i, n in enumerate(nums):
            if i == digitSum(n):
                return i
        return -1
