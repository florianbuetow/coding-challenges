# link: https://leetcode.com/problems/construct-product-matrix/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # O(n*m) time and space

        width, height = len(grid[0]), len(grid)
        def getXY(idx):
            return idx % width, idx // width

        product_left, product_right = [1], [1]
        for i in range(width * height - 1):
            x, y = getXY(i)
            product_left.append(grid[y][x] * product_left[-1])
            product_left[-1] %= 12345

            x, y = getXY(width * height - 1 - i)
            product_right.append(grid[y][x] * product_right[-1])
            product_right[-1] %= 12345

        for i in range(width * height):
            x, y = getXY(i)
            grid[y][x] = (product_left[i] * product_right[-(i+1)]) % 12345
        return grid
