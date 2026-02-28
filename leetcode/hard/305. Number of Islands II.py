# link: https://leetcode.com/problems/number-of-islands-ii/

from typing import List


class UnionFind:
    def __init__(self):
        # O(n) time and O(1) space
        self.land = {}

    def find(self, x):
        # O(n) time and O(1) space
        if x not in self.land:
            self.land[x] = x
        y = self.land[x]
        if y != x:
            y = self.find(y)
        return y

    def mergeIslands(self, x, y):
        # O(n) time and O(1) space
        self.land[self.find(x)] = self.find(y)

    def countIslands(self):
        # O(n) time and O(1) space
        return sum(1 for k, v in self.land.items() if k == v)

    def getNeighbors(self, pos):
        # O(n) time and O(1) space
        self.find(pos)
        neighbors = []
        for nx, ny in zip([pos[0] - 1, pos[0], pos[0] + 1, pos[0]], [pos[1], pos[1] - 1, pos[1], pos[1] + 1]):
            npos = (nx, ny)
            if npos in self.land:
                neighbors.append(npos)
        return neighbors


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # O(n) time and space
        # link: https://leetcode.com/problems/number-of-islands-ii/
        # idea: use union find to join islands as we turn water into land
        result = []
        uf = UnionFind()
        for y, x in positions:
            for pos in uf.getNeighbors((x, y)):
                uf.mergeIslands((x, y), pos)
            result.append(uf.countIslands())
        return result
