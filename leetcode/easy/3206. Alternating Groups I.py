from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/alternating-groups-i/
        n = len(colors)

        def isStartOflternatingGroup(i):
            if colors[i % n] != colors[(i + 1) % n]:
                if colors[(i + 1) % n] != colors[(i + 2) % n]:
                    return True
            return False

        result = 0
        for i in range(n):
            result += [0, 1][isStartOflternatingGroup(i)]
        return result
