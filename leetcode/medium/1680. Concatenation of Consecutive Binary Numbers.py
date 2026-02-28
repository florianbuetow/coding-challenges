class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # O(n log n) time and space
        # link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
        allbits = ""
        for index in range(1, n+1):
            allbits += format(index,"b")
        return int(allbits, 2) % (10**9 + 7)
