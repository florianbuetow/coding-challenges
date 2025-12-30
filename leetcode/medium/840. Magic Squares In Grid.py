# O(n*m) time and O(1) space, n = width, m = height
# link: https://leetcode.com/problems/magic-squares-in-grid

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result = 0
        width, height = len(grid[0]), len(grid)

        def get_grid(x_offset, y_offset): #O(1)
            g = []
            for dy in range(3):
                g.append([])
                for dx in range(3):
                    g[-1].append(grid[y_offset + dy][x_offset + dx])
            return g

        def is_magic_grid(g): # O(1)
            nums = set()
            row_sums = [0] * 3
            col_sums = [0] * 3
            dia_sums = [0] * 2
            for r in range(3):
                for c in range(3):
                    n = g[r][c]
                    row_sums[r] += n
                    col_sums[c] += n
                    if n in nums: return False
                    if n < 1 or n > 9: return False
                    nums.add(n)
                dia_sums[0] += g[r][r]
                dia_sums[1] += g[2-r][r]
            sums = set()
            sums.update(row_sums)
            sums.update(col_sums)
            sums.update(dia_sums)
            return len(sums) == 1

        for y_offset in range(height - 2):
            for x_offset in range(width - 2):
                g = get_grid(x_offset, y_offset)
                if is_magic_grid(g):
                    result += 1
        return result
