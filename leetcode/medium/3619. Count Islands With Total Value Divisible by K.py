# link: https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k

from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # O(n*m) time and space

        width, height = len(grid[0]), len(grid)
        def getLand(pos):
            x, y = pos
            return grid[y][x]

        def getNeighbors(pos):
            res = []
            x, y = pos
            for nx, ny in zip([x-1,x,x+1,x],[y,y-1,y,y+1]):
                if nx < 0 or nx >= width: continue
                if ny < 0 or ny >= height: continue
                if grid[ny][nx] == 0: continue
                res.append((nx, ny))
            return res

        def explore(pos, visited):
            value = 0
            q = deque([pos])
            while q:
                pos = q.popleft()
                if not getLand(pos): continue
                if pos in visited: continue
                visited.add(pos)
                value += getLand(pos)
                for npos in getNeighbors(pos):
                    if npos in visited: continue
                    q.append(npos)
            return value

        result = 0
        visited = set()
        for x in range(width):
            for y in range(height):
                pos = (x, y)
                if pos in visited: continue
                if not getLand(pos): continue
                if explore(pos, visited) % k == 0:
                    result += 1
        return result
