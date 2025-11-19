# O(log n) time and O(1) space
# link: https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 == 0: return 0
        for i in range(1, 61):
            x = num1 - i * num2
            if x < i: continue
            if x.bit_count() <= i:
                return i
        return -1
