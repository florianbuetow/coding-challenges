# O(n) time and O(1) space
# link: https://leetcode.com/problems/find-the-highest-altitude/

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = cur_height = 0
        for delta in gain:
            cur_height += delta
            max_height = max(max_height, cur_height)
        return max_height
