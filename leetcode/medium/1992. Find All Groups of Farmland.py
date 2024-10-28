class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # O(n*m) time and space
        # link: https://leetcode.com/problems/find-all-groups-of-farmland/
        width, height = len(land[0]), len(land)
        result = []
        for x1 in range(width):
            for y1 in range(height):
                if land[y1][x1] == 1:
                    x2, y2 = x1, y1
                    while x2 < width and land[y1][x2] == 1: x2 += 1
                    while y2 < height and land[y2][x1] == 1: y2 += 1
                    for x in range(x1, x2):
                        for y in range(y1, y2):
                            land[y][x] = -1
                    result.append([x1, y1, x2-1, y2-1])
        return result
