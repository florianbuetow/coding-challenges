# link: https://leetcode.com/problems/mirror-distance-of-an-integer


class Solution:
    def mirrorDistance(self, n: int) -> int:
        # O(n) time and O(1) space
        return abs(n - int(str(n)[::-1]))
