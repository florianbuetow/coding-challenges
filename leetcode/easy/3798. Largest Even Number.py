# link: https://leetcode.com/problems/largest-even-number


class Solution:
    def largestEven(self, s: str) -> str:
        # O(n) time and O(1) space
        n = int(s)
        while n % 2 != 0:
            n //= 10
        return str(n) if n else ""
