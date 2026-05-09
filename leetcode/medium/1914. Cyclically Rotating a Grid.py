# link: https://leetcode.com/problems/cyclically-rotating-a-grid/


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # O(n*m) time and O(n+m) space
        width, height = len(grid[0]), len(grid)

        def idxToPos(w, h, idx):
            if idx < h - 1: return idx, 0
            if idx < h + w - 2: return h - 1, idx - h + 1
            if idx < 2 * h + w - 3: return 2 * h + w - 3 - idx, w - 1
            return 0, 2 * h + 2 * w - 4 - idx

        def rotateBand(xs, ys, w, h, k):
            circumfence = 2 * w + 2 * h - 4
            k %= circumfence
            if not k: return

            visited = set()
            for start in range(circumfence):
                curr = start
                y, x = idxToPos(w, h, curr)
                val = grid[xs + y][ys + x]
                while curr not in visited:
                    visited.add(curr)
                    next = (curr + k) % circumfence
                    ny, nx = idxToPos(w, h, next)
                    grid[xs + ny][ys + nx], val = val, grid[xs + ny][ys + nx]
                    curr = next

        for d in range(min(width, height) // 2):
            rotateBand(d, d, width - 2 * d, height - 2 * d, k)
        return grid
