# link: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # O(n*m) time and space
        width, height = len(grid[0]), len(grid)

        def getNeighbors(x, y):
            typ = grid[y][x]
            res, tmp = [], []
            if typ in [1,3,5]: tmp.append([-1, 0]) # left
            if typ in [1,4,6]: tmp.append([+1, 0]) # right
            if typ in [2,5,6]: tmp.append([0, -1]) # up
            if typ in [2,3,4]: tmp.append([0, +1]) # down
            for dx, dy in tmp:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= width: continue
                if ny < 0 or ny >= height: continue
                ntyp = grid[ny][nx]
                valid = False
                if dx == -1 and ntyp in [1, 4, 6]: valid = True # left
                if dx == +1 and ntyp in [1, 3, 5]: valid = True # right
                if dy == -1 and ntyp in [2, 3, 4]: valid = True # up
                if dy == +1 and ntyp in [2, 5, 6]: valid = True # down
                if valid:
                    res.append((nx, ny))
            return res

        start, goal = (0, 0), (width -1, height -1)
        visited = set()
        stack = [start]
        while stack:
            pos = stack.pop()
            if pos in visited: continue
            if pos == goal: return True
            visited.add(pos)
            for pos in getNeighbors(*pos):
                stack.append(pos)
        return False
