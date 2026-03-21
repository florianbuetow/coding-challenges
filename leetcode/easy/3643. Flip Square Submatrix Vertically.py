# link: https://leetcode.com/problems/flip-square-submatrix-vertically/

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # O(k*k) time and O(1) space
        x, y = y, x
        top, btm = y, y + k - 1
        while top < btm:
            for px in range(x, x + k):
                grid[btm][px], grid[top][px] = grid[top][px], grid[btm][px]
            top += 1
            btm -= 1
        return grid
