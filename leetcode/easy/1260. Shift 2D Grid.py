# link: https://leetcode.com/problems/shift-2d-grid/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # O(n * m) time and space
        width, height = len(grid[0]), len(grid)

        def getCoords(pos):
            y = (pos // width) % height
            x = pos % width
            return x, y

        def getValue(pos):
            x, y = getCoords(pos)
            return grid[y][x]

        def setValue(pos, value):
            x, y = getCoords(pos)
            grid[y][x] = value

        moved = set()
        for i in range(0, width*height):
            if i in moved:
                continue
            value = getValue(i)
            while i not in moved:
                moved.add(i)
                i = (i + k) % (width * height)
                tmp = getValue(i)
                setValue(i, value)
                value = tmp
        return grid
