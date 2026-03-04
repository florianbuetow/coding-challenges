# link: https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # O(n * n) time and O(n) space
        row_pos = {}
        for row in range(len(mat)):
            row_sum = sum(mat[row])
            if row_sum != 1: continue
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    row_pos[row] = col
                    break

        col_pos = {}
        for col in range(len(mat[0])):
            col_sum = sum([mat[row][col] for row in range(len(mat))])
            if col_sum != 1: continue
            for row in range(len(mat)):
                if mat[row][col] == 1:
                    col_pos[col] = row
                    break

        counter = 0
        for row, col in row_pos.items():
            if col in col_pos and col_pos[col] == row:
                counter += 1
        return counter
