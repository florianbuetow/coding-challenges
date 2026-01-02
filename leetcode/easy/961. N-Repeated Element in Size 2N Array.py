# O(n) time and space
# link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

from collections import defaultdict
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        n = len(nums) // 2
        for num in nums:
            counter[num] += 1
        for num, count in counter.items():
            if count == n:
                return num
        return -1
