from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # O(n* m) time and O(n) space, with n,m being the width and height of the matrix
        # link: https://leetcode.com/problems/maximal-rectangle/
        # idea:
        #    Transform matrix into a histogram at each row where matrix[row][col] is the height in the histogram from row to the top
        #    Then for each row, compute max rectangle area in the histogram that starts at the current row

        width, height = len(matrix[0]), len(matrix)
        for col in range(width):
            h = 0
            for row in range(height):
                if matrix[row][col] == '1':
                    h += 1
                else:
                    h = 0
                matrix[row][col] = h

        max_area = 0
        for cur_row in range(height):
            stack = []
            for cur_col in range(width):
                cur_h = matrix[cur_row][cur_col]
                new_col = cur_col
                while stack and stack[-1][0] > cur_h:
                    prev_h, prev_col = stack.pop()
                    area = (cur_col - prev_col) * prev_h
                    max_area = max(area, max_area)
                    new_col = prev_col
                stack.append([cur_h, new_col])

            while stack:
                prev_h, prev_col = stack.pop()
                area = (width - prev_col) * prev_h
                max_area = max(area, max_area)

        return max_area

