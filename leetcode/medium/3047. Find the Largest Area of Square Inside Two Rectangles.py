# O(n*n) time and O(1) space
# link: https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        result = 0
        for i in range(len(bottomLeft)):
            p1, p2 = bottomLeft[i], topRight[i]
            for j in range(i + 1, len(bottomLeft)):
                p3, p4 = bottomLeft[j], topRight[j]
                width = min(p2[0], p4[0]) - max(p1[0], p3[0])
                height = min(p2[1], p4[1]) - max(p1[1], p3[1])
                result = max(result, max(0, min(width, height)) ** 2)
        return result
