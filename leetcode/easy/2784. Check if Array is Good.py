# link: https://leetcode.com/problems/check-if-array-is-good/

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # O(n) time and O(1) space
        count_n = summ = 0
        for i, n in enumerate(nums, start=1):
            if n == len(nums) - 1:
                count_n += 1
            summ |= (1 << n)
        return count_n == 2 and summ == (1 << len(nums)) - 2
