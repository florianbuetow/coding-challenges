from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # O((n*m)*4^(n*m)) time and O(n*m) space
        # link: https://leetcode.com/problems/path-with-maximum-gold/
        width, height = len(grid[0]), len(grid)
        
        def getNeighbors(pos):
            lst = []
            x, y = pos
            for nx, ny in zip([x-1,x,x+1,x],[y,y-1,y,y+1]):
                if nx < 0 or nx >= width: continue
                if ny < 0 or ny >= height: continue
                if grid[ny][nx] != 0: lst.append((nx, ny))
            return lst
        
        def getMaxPath(pos, visited):
            max_sub_path = 0
            if pos not in visited:
                visited.add(pos)
                for neighbor in getNeighbors(pos):
                    sub_path = getMaxPath(neighbor, visited)
                    max_sub_path = max(max_sub_path, sub_path)
                visited.remove(pos)
                max_sub_path += grid[pos[1]][pos[0]]
            return max_sub_path
        
        result = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] != 0:
                    result = max(result, getMaxPath((x, y), set()))
        return result