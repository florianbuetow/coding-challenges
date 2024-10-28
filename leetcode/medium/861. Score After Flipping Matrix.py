from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # O(n * m) time and O(1) space
        # link: https://leetcode.com/problems/score-after-flipping-matrix/
        width, height = len(grid[0]), len(grid)

        def countBitsInCol(col):
            count = 0
            for row in range(height):
                count += grid[row][col]
            return count

        def getRowValue(row):
            value = 0
            tmp = []
            for col in range(width):
                bit = grid[row][col]
                value = value * 2 + bit
                tmp.append(bit)
                tmp.append(value)
            return value

        for row in range(height):
            if grid[row][0] == 0:
                for col in range(width):
                    grid[row][col] = 1 - grid[row][col]

        for col in range(width):
            if countBitsInCol(col) <= height // 2:
                for row in range(height):
                    grid[row][col] = 1 - grid[row][col]

        result = 0
        for row in range(height):
            result += getRowValue(row)
        return result