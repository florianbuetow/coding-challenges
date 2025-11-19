# O(n*n*n) time and O(1) space
# link: https://leetcode.com/problems/largest-triangle-area/

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calcArea(p1, p2, p3):
            area  = p1[0] * (p2[1] - p3[1])
            area -= p2[0] * (p1[1] - p3[1])
            area += p3[0] * (p1[1] - p2[1])
            return abs(area) / 2.0

        max_area = 0
        for i in range(len(points)):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1 == p2: continue
                for k in range(j + 1, len(points)):
                    p3 = points[k]
                    if p1 == p3: continue
                    if p2 == p3: continue
                    cur_area = calcArea(p1, p2, p3)
                    max_area = max(max_area, cur_area)
        return max_area
