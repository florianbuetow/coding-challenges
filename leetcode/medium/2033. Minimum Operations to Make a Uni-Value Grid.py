# link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # O(n*m) time and O(1) space
        width, height = len(grid[0]), len(grid)
        counter = [0] * 10001

        min_n = max_n = grid[0][0]
        for row in grid:
            for n in row:
                counter[n] += 1
                if abs(grid[0][0] - n) % x != 0:
                    return -1
                min_n, max_n = min(min_n, n), max(max_n, n)

        idx = median = min_n
        acc, target = 0, (width * height + 1) // 2
        while idx <= max_n:
            acc += counter[idx]
            if acc >= target:
                median = idx
                break
            idx += x

        idx, result = min_n, 0
        while idx <= max_n:
            result += abs(median - idx) // x * counter[idx]
            idx += x
        return result
