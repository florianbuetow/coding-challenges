# O(n) time and O(1) space
# link: https://leetcode.com/problems/make-array-elements-equal-to-zero/

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        result = 0
        left_sum = 0
        total = sum(nums)
        for i, n in enumerate(nums):
            remaining = total - left_sum
            if n == 0:
                if left_sum == remaining:
                    result += 2 # can start from here in either direction
                elif abs(remaining - left_sum) == 1:
                    result += 1 # have to start into the direction where the sum on the left of i vs the summ on the right of i is 1 more than on the other side
            left_sum += n
        return result
