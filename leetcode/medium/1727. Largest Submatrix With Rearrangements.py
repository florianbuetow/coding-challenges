# link: https://leetcode.com/problems/largest-submatrix-with-rearrangements/

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # O(n^2 log n) time and O(n) space, n = max(width, height)
        width, height = len(matrix[0]), len(matrix)
        result = 0
        for i in range(1, height):
            for j in range(width):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        for i in range(height):
            matrix[i].sort(reverse=True)
            for j in range(width):
                result = max(result, matrix[i][j] * (j + 1))
        return result
