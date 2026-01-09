# O(log n) time and space, n = int(s)
# link: https://leetcode.com/problems/largest-even-number

class Solution:
    def largestEven(self, s: str) -> str:
        n = int(s)
        while n % 2 != 0:
            n //= 10
        return str(n) if n else ""
