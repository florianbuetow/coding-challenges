class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # O(n*m) time and space, n,m = width and height of the matrix
        result = []
        for col in range(len(matrix[0])):
            max_val = -float('inf')
            for row in range(len(matrix)):
                val = matrix[row][col]
                max_val = max(val, max_val)
            for row in matrix:
                if min(row) == max_val:
                    result.append(max_val)
                    break
        return result