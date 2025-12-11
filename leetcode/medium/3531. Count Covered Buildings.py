# O(n) time and space
# link: https://leetcode.com/problems/count-covered-buildings/

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        minmax_x = defaultdict(list)
        minmax_y = defaultdict(list)
        for x, y in buildings:
            minmax_x[x].append(y)
            minmax_y[y].append(x)
            minmax_x[x] = [min(minmax_x[x]), max(minmax_x[x])]
            minmax_y[y] = [min(minmax_y[y]), max(minmax_y[y])]

        result = 0
        for x, y in buildings:
            if minmax_x[x][0] < y < minmax_x[x][1]:
                if minmax_y[y][0] < x < minmax_y[y][1]:
                    result += 1
        return result
