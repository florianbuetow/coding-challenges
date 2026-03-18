# link: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # O(n*m) time and O(1) space
        result = 0
        width, height = len(grid[0]), len(grid)
        x, summ = width-1, 0
        for y in range(height):
            for z in range(x+1):
                summ += grid[y][z]
            while summ > k and x >=0:
                for z in range(y+1):
                    summ -= grid[z][x]
                x -= 1
            if x < 0: break
            result += (x+1)
        return result
