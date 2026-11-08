# link: https://leetcode.com/problems/count-servers-that-communicate/

from collections import defaultdict


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # O(n*m) time and O(n+m) space
        rows = defaultdict(int)
        cols = defaultdict(int)
        for r, row in enumerate(grid):
            for c, count in enumerate(row):
                if count:
                    cols[c] += 1
                    rows[r] += 1
        result = 0
        for r, row in enumerate(grid):
            for c, count in enumerate(row):
                if count and cols[c] + rows[r] > 2:
                    result += 1
        return result
