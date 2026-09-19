# link: https://leetcode.com/problems/circle-and-rectangle-overlapping/

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # O(1) time and space

        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        def projection(point, line):
            x, y = point
            x1, y1 = line[0]
            x2, y2 = line[1]            
            dx = x2 - x1
            dy = y2 - y1
            denom = dx * dx + dy * dy
            if denom == 0: return [x1, y1]
            t = (x - x1) * dx + (y - y1) * dy
            t = t / denom
            t = max(0, min(1, t))

            px = x1 + t * dx
            py = y1 + t * dy
            return [px, py]

        circle = [xCenter, yCenter]
        points = [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]
        for p1 in points:
            for p2 in points:
                line = [p1, p2]
                point = projection(circle, line)
                if distance(circle, point) <= radius: return True
        return False
