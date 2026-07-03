# link: https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

from collections import defaultdict, deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # O(n * m) time and space
        width, height = len(grid[0]), len(grid)
        costs = defaultdict(int)

        def getValidNeighbors(pos, health):
            neighbors = []
            x, y = pos
            for dx, dy in zip([-1,0,1,0],[0,-1,0,1]):
                px, py = x + dx, y + dy
                if px < 0 or px >= width: continue
                if py < 0 or py >= height: continue
                neighbors.append((px, py))
            return neighbors

        start = (0, 0)
        goal = (width-1, height-1)

        start_health = health - grid[0][0]
        costs[start] = start_health

        q = deque([[start_health, start]])
        while q:
            health, pos = q.popleft()
            if health <= 0: continue

            if health < costs[pos]: continue
            if pos == goal: return True

            for npos in getValidNeighbors(pos, health):
                dh = grid[npos[1]][npos[0]]
                next_health = health - dh

                if npos not in costs or costs[npos] < next_health:
                    costs[npos] = next_health
                    q.append([next_health, npos])
        return False
