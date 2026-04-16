# link: https://leetcode.com/problems/closest-equal-element-queries/

import bisect
from collections import defaultdict
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # O(n log m) time and O(m) space, n=len(queries), m = len(nums)

        def buildIndex():
            index = defaultdict(list)
            for i, n in enumerate(nums):
                index[n].append(i)
            return index

        def findClosest(index, pos):
            n = nums[pos]
            res = float('inf')
            arr = index[n]

            if len(arr) > 1:
                idx = bisect.bisect_left(arr, pos)

                left_i = arr[(idx - 1) % len(arr)]
                right_i = arr[(idx + 1) % len(arr)]

                dist_left = min(abs(left_i - pos), len(nums) - abs(left_i - pos))
                dist_right = min(abs(right_i - pos), len(nums) - abs(right_i - pos))

                res = min(dist_left, dist_right)

            return [res, -1][res == float('inf')]

        index = buildIndex()
        return [findClosest(index, pos) for pos in queries]
