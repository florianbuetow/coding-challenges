# O(log n) time and space
# link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        result = 0
        if n:
            result += sum([int(digit) for digit in str(n) if digit != '0'])
            result *= int(''.join([digit for digit in str(n) if digit != '0']))
        return result
