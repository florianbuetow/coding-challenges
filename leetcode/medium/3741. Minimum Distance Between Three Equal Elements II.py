# link: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # O(n) time and space

        lookup = defaultdict(list)
        for i, n in enumerate(nums):
            lookup[n].append(i)

        result = float('inf')
        for indices in lookup.values():
            for i in range(len(indices)-2):
                a, b, c = indices[i], indices[i+1], indices[i+2]
                result = min(
                    result,
                    abs(a - b) + abs(b - c) + abs(c - a)

                )
        if result == float('inf'): result = -1
        return result
