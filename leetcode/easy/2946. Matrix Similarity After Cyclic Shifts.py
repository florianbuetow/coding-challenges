# link: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # O(n*m) time and O(m) space
        width, height = len(mat[0]), len(mat)
        for row in range(height):
            k *= -1
            tmp = []
            for col in range(width):
                col_shifted = (col + k) % width
                tmp.append(mat[row][col_shifted])
            for col in range(width):
                if mat[row][col] != tmp[col]:
                    return False
        return True
