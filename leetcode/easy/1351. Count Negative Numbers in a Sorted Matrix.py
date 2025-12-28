# O(m + n) time and O(1) space
# link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        pos = len(grid[0]) - 1
        for row in grid:
            while pos >= 0 and row[pos] < 0:
                pos -= 1
            result += len(row) - (pos + 1)
        return result
