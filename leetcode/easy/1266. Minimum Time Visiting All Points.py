# O(n) time and O(1) space
# link: https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def dist(a, b):
            dx = abs(a[0]-b[0])
            dy = abs(a[1]-b[1])
            return dx + dy - min(dx, dy)

        result = 0
        for i in range(1, len(points)):
            result += dist(points[i-1], points[i])
        return result
