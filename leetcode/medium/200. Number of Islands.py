from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(width*height) time and space
        width, height = len(grid[0]), len(grid)

        def isUnvisitedLand(x, y, visited):
            return (x, y) not in visited and grid[y][x] == '1'

        def getUnvisitedNeighboringLand(pos, visited):
            neighbors = []
            x, y = pos
            for nx, ny in zip([x-1,x,x+1,x],[y,y-1,y,y+1]):
                if nx < 0 or nx >= width: continue
                if ny < 0 or ny >= height: continue
                if isUnvisitedLand(nx, ny, visited):
                    neighbors.append((nx, ny))
            return neighbors

        def exploreIsland(pos, visited):
            q = deque([pos])
            while q:
                pos = q.popleft()
                if pos not in visited:
                    visited.add(pos)
                    for npos in getUnvisitedNeighboringLand(pos, visited):
                        q.append(npos)

        found_islands = 0
        visited = set()
        for y in range(height):
            for x in range(width):
                if isUnvisitedLand(x, y, visited):
                    exploreIsland((x, y), visited)
                    found_islands += 1
        return found_islands
