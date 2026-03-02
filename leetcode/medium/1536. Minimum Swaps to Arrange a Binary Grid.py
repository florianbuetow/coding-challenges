# link: https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

class Solution:
    def minSwaps(self, grid):
        # O(n*n) time and O(n) space
        result = 0
        n = len(grid)
        leading_zeros = []
        for row in grid:
            leading_zeros.append(0)
            for col in range(n-1, -1, -1):
                if row[col] != 0: break
                leading_zeros[-1] += 1

        for row in range(n):
            needed = n-row-1
            col = row
            while col < n:
                if leading_zeros[col] >= needed: break
                col += 1
            if col == n: return -1
            while col > row:
                tmp = leading_zeros[col]
                leading_zeros[col] = leading_zeros[col-1]
                leading_zeros[col-1] = tmp
                col -= 1
                result += 1
        return result
