class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # O(n * m) time and O(1) space
        width, height = len(grid[0]), len(grid)

        def countSidesWithWater(x, y):
            count = 0
            for nx, ny in zip([x-1,x,x+1,x],[y,y+1,y,y-1]):
                if nx < 0 or nx >= width:
                    count += 1
                    continue
                elif ny < 0 or ny >= height:
                    count += 1
                    continue
                elif grid[ny][nx] == 0:
                    count += 1
            return count

        result = 0
        for x in range(width):
            for y in range(height):
                if grid[y][x] == 1:
                    result += countSidesWithWater(x, y)
        return result