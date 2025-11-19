# O(k log k) time and O(k) space
# link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        visited = set()
        heap = []

        def addPair(pair):
            if pair[0] >= len(nums1): return
            if pair[1] >= len(nums2): return
            if pair in visited: return
            pair_sum = nums1[pair[0]] + nums2[pair[1]]
            heappush(heap, (pair_sum, pair))
            visited.add(pair)

        def getPairAsValues(pair):
            return [nums1[pair[0]], nums2[pair[1]]]

        addPair((0, 0))
        while heap and len(result) < k:
            _, pair = heappop(heap)
            result.append(getPairAsValues(pair))
            for next_pair in [(pair[0] + 1, pair[1]), (pair[0], pair[1] + 1)]:
                addPair(next_pair)
        return result
