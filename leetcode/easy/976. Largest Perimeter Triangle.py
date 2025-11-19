# O(nlogn) time and O(1) space
# link: https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, sides: List[int]) -> int:
        sides.sort(reverse=True)
        for i in range(len(sides)-2):
            c, b, a = sides[i], sides[i+1], sides[i+2]
            if a + b > c: return a + b + c
        return 0
