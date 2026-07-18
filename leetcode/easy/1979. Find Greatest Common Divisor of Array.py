# link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # O(log n) time and O(1) space
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        return gcd(min(nums), max(nums))
