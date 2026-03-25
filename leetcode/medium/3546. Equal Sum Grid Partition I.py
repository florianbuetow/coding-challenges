# link: https://leetcode.com/problems/equal-sum-grid-partition-i/

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # O(n*m) time and O(1) space

        def getGridSum(grid):
            summ = 0
            width, height = len(grid[0]), len(grid)
            for y in range(height):
                for x in range(width):
                    summ += grid[y][x]
            return summ

        def canPartitionHorizontal(grid):
            top_sum, btm_sum = 0, getGridSum(grid)
            for row in grid:
                if top_sum == btm_sum: return True
                top_sum += sum(row)
                btm_sum -= sum(row)
            return top_sum == btm_sum

        def canPartitionVertical(grid):
            lft_sum, rgt_sum = 0, getGridSum(grid)
            for x in range(len(grid[0])):
                if lft_sum == rgt_sum: return True
                for y in range(len(grid)):
                    lft_sum += grid[y][x]
                    rgt_sum -= grid[y][x]
            return lft_sum == rgt_sum

        return canPartitionHorizontal(grid) or canPartitionVertical(grid)
