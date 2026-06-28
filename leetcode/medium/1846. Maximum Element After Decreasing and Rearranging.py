# link: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

from collections import defaultdict
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # O(n) time and space
        freq = defaultdict(int)
        for n in arr:
            idx = min(n, len(arr))
            freq[idx] += 1
        result = 0
        for i in range(len(arr)):
            idx = i + 1
            result = min(idx, result + freq[idx])
        return result
