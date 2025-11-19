# O(n*n log n*n) time and O(n*n) space
# link: https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def getNeighbors(pos):
            neighbors = []
            x, y = pos
            for nx, ny in zip([x-1,x,x+1,x],[y,y-1,y,y+1]):
                if nx < 0 or nx >= n: continue
                if ny < 0 or ny >= n: continue
                nh = grid[ny][nx]
                npos = (nx, ny)
                neighbors.append([nh, npos])
            return neighbors

        start, goal = (0, 0), (n-1, n-1)
        t = 0
        visited = set()
        q = [[grid[0][0],start]]
        while True:
            while q[0][0] <= t:
                h, pos = heappop(q)
                if pos in visited: continue
                if pos == goal: return t
                visited.add(pos)
                for nh, npos in getNeighbors(pos):
                    heappush(q, [nh, npos])
            t = q[0][0]
