from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # O(n*m) time and O(n) space, n:=width, m:=height
        # link: https://leetcode.com/problems/minimum-falling-path-sum-ii/

        def calculatePredecessorRow(row):
            # first find the two smallest elements in the row
            smallest = []
            for col in range(len(row)):
                smallest.append([row[col], col])
                if len(smallest) > 2:
                    smallest.sort()
                    smallest.pop()
            ret = []
            for col in range(len(row)):
                if col != smallest[0][1]:  # predecessor can't be in the same column
                    ret.append(smallest[0][0])
                else:
                    ret.append(smallest[1][0])
            return ret

        width = len(grid[0])
        if width == 1:
            return grid[0][0]
        min_predecessors = [0] * width
        for row in grid:
            curr = []
            for col in range(width):
                curr.append(min_predecessors[col] + row[col])
            min_predecessors = calculatePredecessorRow(curr)
        return min(curr)
