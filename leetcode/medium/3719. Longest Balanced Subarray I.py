# link: https://leetcode.com/problems/longest-balanced-subarray-i/


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        result = 0
        for left in range(len(nums)):
            counters = [set(), set()]
            for right in range(left, len(nums)):
                n = nums[right]
                counters[n % 2].add(n)
                if len(counters[0]) == len(counters[1]):
                    result = max(result, right - left + 1)
        return result
