# O(n^4) time and O(n^2) space
# link: https://adventofcode.com/2025/day/9

class NonConvexPolygon:

    def __init__(self, points):
        self.points = points

    def contains(self, point):
        x, y = point
        crossings = 0
        for i in range(len(self.points)):
            v1 = self.points[i]
            v2 = self.points[(i + 1) % len(self.points)]
            x1, y1 = v1
            x2, y2 = v2

            if (x, y) == (x1, y1) or (x, y) == (x2, y2): return True
            if (y1 == y2 and y1 == y) and (min(x1, x2) <= x <= max(x1, x2)): return True
            if (x1 == x2 and x1 == x) and (min(y1, y2) <= y <= max(y1, y2)): return True

            if x1 == x2:
                if min(y1, y2) <= y <= max(y1, y2):
                    if x1 > x:
                        if min(y1, y2) < y < max(y1, y2):
                            crossings += 1
                        elif y == min(y1, y2):
                            crossings += 1
        return crossings % 2 == 1

class Solution:

    def largestRectangleOfRedTiles(self, filename) -> int:

        def loadRedTiles(filename):
            tiles = []
            with open(filename, "r") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        x, y = [int(value) for value in line.split(',')]
                        tiles.append([x, y])
            return tiles

        def getArea(p1, p2):
            return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

        tiles = loadRedTiles(filename)
        polygon_checker = NonConvexPolygon(tiles)

        all_x = sorted(set(t[0] for t in tiles))
        all_y = sorted(set(t[1] for t in tiles))
        x_to_idx = {x: i for i, x in enumerate(all_x)}
        y_to_idx = {y: i for i, y in enumerate(all_y)}

        inside = [[polygon_checker.contains((x, y)) for x in all_x] for y in all_y]

        def isRectangleInside(cornerOne, cornerTwo):
            xi1, yi1 = x_to_idx[cornerOne[0]], y_to_idx[cornerOne[1]]
            xi2, yi2 = x_to_idx[cornerTwo[0]], y_to_idx[cornerTwo[1]]
            xi_min, xi_max = min(xi1, xi2), max(xi1, xi2)
            yi_min, yi_max = min(yi1, yi2), max(yi1, yi2)

            for yi in range(yi_min, yi_max + 1):
                for xi in range(xi_min, xi_max + 1):
                    if not inside[yi][xi]:
                        return False
            return True

        result = 0
        pair_count = 0
        total_pairs = len(tiles) * (len(tiles) - 1) // 2
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                pair_count += 1
                if isRectangleInside(tiles[i], tiles[j]):
                    result = max(result, getArea(tiles[i], tiles[j]))
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleOfRedTiles('input_0.txt'))
    print(s.largestRectangleOfRedTiles('input_1.txt'))


