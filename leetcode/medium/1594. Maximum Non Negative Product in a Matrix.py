# link: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # O(n*m) time and O(n) space
        width, height = len(grid[0]), len(grid)
        for y in range(height):
            for x in range(width):
                candidates = []

                value = grid[y][x]
                if y == 0 and x == 0:
                    grid[y][x] = [value, value]
                    continue

                if x > 0:
                    factor1 = grid[y][x-1]
                    candidates.append(value * factor1[0])
                    candidates.append(value * factor1[1])

                if y > 0:
                    factor2 = grid[y-1][x]
                    candidates.append(value * factor2[0])
                    candidates.append(value * factor2[1])

                grid[y][x] = [
                    min(candidates),
                    max(candidates),
                ]

        result = grid[-1][-1][1]
        if result < 0: return -1
        return result  % (10**9+7)
