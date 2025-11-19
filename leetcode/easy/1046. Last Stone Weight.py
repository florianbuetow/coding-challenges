# O(n log n) time and O(1) space
# link: https://leetcode.com/problems/last-stone-weight/

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapify(stones)
        while len(stones) > 1:
            y = heappop(stones)
            x = heappop(stones)
            if x != y:
                heappush(stones, -abs(x - y))
        return -stones[0] if stones else 0
