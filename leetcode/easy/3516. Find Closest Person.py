# O(1) time and space
# link: https://leetcode.com/problems/find-closest-person/

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        def dist(a, b):
            return abs(a - b)

        diff = dist(x,z) - dist(y,z)
        if diff < 0: return 1
        if diff > 0: return 2
        return 0
