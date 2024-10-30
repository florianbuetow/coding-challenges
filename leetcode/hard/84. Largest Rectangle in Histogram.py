from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # O(n) time and space
        # link: https://leetcode.com/problems/largest-rectangle-in-histogram/
        max_area = 0
        stack = []
        for index, height in enumerate(heights):
            insert_index = index
            while stack and stack[-1][0] > height:
                h, i = stack.pop()
                area = (index - i) * h
                max_area = max(area, max_area)
                insert_index = i
            stack.append([height, insert_index])

        index = len(heights)
        while stack:
            h, i = stack.pop()
            area = h * (index - i)
            max_area = max(area, max_area)

        return max_area