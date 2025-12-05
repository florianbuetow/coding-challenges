# O(n log n) time and O(1) space
# link: https://leetcode.com/problems/minimum-cost-to-connect-sticks

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        result = 0
        heapify(sticks)
        while len(sticks) > 1:
            stick = heappop(sticks) + heappop(sticks)
            result += stick
            heappush(sticks, stick)
        return result
