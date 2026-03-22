# link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # O(n*n) time and space
        length = len(mat)

        def equals(mat_a, mat_b):
            for y in range(length):
                for x in range(length):
                    if mat_a[y][x] != mat_b[y][x]: return False
            return True

        def rotate(matrix):
            return [[matrix[j][i] for j in range(length)] for i in range(length - 1, -1, -1)]

        if equals(mat, target): return True
        for _ in range(3):
            target = rotate(target)
            if equals(mat, target): return True
        return False
