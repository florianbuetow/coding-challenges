# O(m*n log m*n) time and O(m*n) space, m = height, n = width
# link: https://leetcode.com/problems/trapping-rain-water-ii/

from heapq import heappush, heappop, heapify
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        height, width = len(heightMap), len(heightMap[0])

        def buildBoundaryHeap():
            boundary = []
            boundary_cells = set()
            for x in range(width):
                for y in [0, height-1]:
                    pos = (x, y)
                    h = heightMap[y][x]
                    boundary.append([h, pos])
                    boundary_cells.add(pos)
            for x in [0, width - 1]:
                for y in range(1, height-1):
                    h = heightMap[y][x]
                    pos = (x, y)
                    boundary.append([h, pos])
                    boundary_cells.add(pos)
            heapify(boundary)
            return boundary, boundary_cells

        def getNeighbors(pos):
            neighbors = []
            x, y = pos
            for dx, dy in zip([-1,0,1,0], [0,-1,0,1]):
                px, py = dx + x, dy + y
                if px < 0 or px >= width: continue
                if py < 0 or py >= height: continue
                neighbors.append([heightMap[py][px], (px, py)])
            return neighbors

        result = 0
        visited = set()
        boundary, boundary_cells = buildBoundaryHeap()
        while boundary:
            h, pos = heappop(boundary)
            if pos in visited: continue
            visited.add(pos)
            for neighbor in getNeighbors(pos):
                nh, npos = neighbor
                if npos in visited: continue
                # if npos in boundary_cells: continue
                if nh >= h:
                    heappush(boundary, neighbor)
                else:
                    result += h - nh
                    heightMap[npos[1]][npos[0]] = h
                    heappush(boundary, [h, npos])
                    boundary_cells.add(npos)
        return result
