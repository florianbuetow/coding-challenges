# O(n*m*k) time and O(n*m*k) space
# link: https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k

from functools import cache
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        width, height = len(grid[0]), len(grid)

        @cache
        def helper(x, y, path_sum):
            result = 0
            path_sum += grid[y][x]
            path_sum %= k
            if (x, y) == (width - 1, height - 1):
                if path_sum == 0:
                    result += 1
            else:
                for nx, ny in zip([x, x+1], [y+1, y]):
                    if nx >= width: continue
                    if ny >= height: continue
                    result += helper(nx, ny, path_sum)
                    result %= 10 ** 9 + 7
            return result

        return helper(0, 0, 0)
