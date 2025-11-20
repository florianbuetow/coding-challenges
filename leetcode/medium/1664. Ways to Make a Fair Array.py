# O(n) time and space
# link: https://leetcode.com/problems/ways-to-make-a-fair-array/

from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        result = 0
        left_even, right_even = 0, sum(nums[i] for i in range(0, len(nums), 2))
        left_odd, right_odd = 0, sum(nums[i] for i in range(1, len(nums), 2))
        for i, n in enumerate(nums):
            if i % 2 == 0:
                right_even -= n
            else:
                right_odd -= n

            even_sum = left_even + right_odd
            odd_sum = left_odd + right_even
            if even_sum == odd_sum:
                result += 1

            if i % 2 == 0:
                left_even += n
            else:
                left_odd += n

        return result
