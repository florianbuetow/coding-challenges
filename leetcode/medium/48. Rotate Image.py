# link: https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(n*n) time and O(1) space

        # 1. flip rows
        top, bottom = 0, len(matrix) - 1
        while top < bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -=1

        # 2. traspose matrix along row=col diagonal
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        return matrix
