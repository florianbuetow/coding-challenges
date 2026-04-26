# link: https://leetcode.com/problems/detect-cycles-in-2d-grid/

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # O(n*m) time and space
        height, width = len(grid), len(grid[0])

        visited = set()
        def helper(curr, prev):
            visited.add(curr)
            x, y = curr
            for nx, ny in zip([x,x-1,x,x+1],[y+1,y,y-1,y]):
                next = (nx, ny)
                if next != prev:
                    if 0 <= nx < width:
                        if 0 <= ny < height:
                            if grid[ny][nx] == grid[y][x]:
                                if next in visited: return True
                                if helper(next, curr): return True
            return False

        for y in range(height):
            for x in range(width):
                pos = (x, y)
                if pos in visited: continue
                if helper(pos, None): return True
        return False
