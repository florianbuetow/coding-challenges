from functools import cache
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # O(n*m) time and space, n = width, m = height
        # link: https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/submissions/
        width, height = len(grid[0]), len(grid)

        @cache
        def getMoves(pos):
            moves = []
            x, y = pos
            val = grid[y][x]
            for dx, dy in zip([1, 1, 1], [-1, 0, 1]):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= width: continue
                if ny < 0 or ny >= height: continue
                if val >= grid[ny][nx]: continue
                moves.append((nx, ny))
            return moves

        @cache
        def findLongestPath(pos, path_len):
            result = path_len
            moves = getMoves(pos)
            for npos in moves:
                result = max(result, findLongestPath(npos, path_len + 1))
            return result

        result = 0
        for col in range(height):
            result = max(result, findLongestPath((0, col), 0))
        return result
