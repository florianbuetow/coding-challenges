# link: https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # O(n) time and O(1) space
        left = sum(1 for m in moves if m == 'L')
        right = sum(1 for m in moves if m == 'R')
        return abs(left - right) + len(moves) - left - right
