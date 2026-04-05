# link: https://leetcode.com/problems/robot-return-to-origin/

from collections import defaultdict


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # O(n) time and O(1) space
        counters = defaultdict(int)
        for m in moves:
            counters[m] += 1
        return counters['U'] == counters['D'] and counters['L'] == counters['R']
