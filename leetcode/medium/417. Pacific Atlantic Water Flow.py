# O(n*m) time and space where n, m = width, height
# link: https://leetcode.com/problems/pacific-atlantic-water-flow/

from collections import deque
class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        width, height = len(grid[0]), len(grid)

        def getUphillOrLevelNeighbors(pos):
            neigbors = []
            x, y = pos
            for nx, ny in zip([x-1,x+0,x+1,x+0],[y+0,y-1,y+0,y+1]):
                if nx < 0 or nx >= width: continue
                if ny < 0 or ny >= height: continue
                if grid[ny][nx] < grid[y][x]: continue
                neigbors.append((nx, ny))
            return neigbors

        def getReachablePeaks(seed):
            visited = set()
            q = deque(seed)
            while q:
                pos = q.popleft()
                if pos in visited: continue
                visited.add(pos)
                for npos in getUphillOrLevelNeighbors(pos):
                    q.append(npos)
            return visited

        seed = []
        for x in range(width): seed.append((x, 0))
        for y in range(height): seed.append((0, y))
        pacific = getReachablePeaks(seed)

        seed = []
        for x in range(width): seed.append((x, height-1))
        for y in range(height): seed.append((width-1, y))
        atlantic = getReachablePeaks(seed)

        result = []
        for pos in pacific:
            if pos in atlantic:
                x, y = pos
                result.append([y, x])
        return result
