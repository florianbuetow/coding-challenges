# link: https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/


from collections import defaultdict

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # O(n) time and O(1) space
        counters = defaultdict(int)
        for n in nums:
            key = n % value
            counters[key] += 1

        mex = float('inf')
        for key in range(value):
            mex = min(mex, counters[key] * value + key)
        return mex
