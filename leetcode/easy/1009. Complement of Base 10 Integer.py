# link: https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # O(log n) time and space
        bits = []
        while n or not bits:
            bits.append((n+1) % 2)
            n //=2
        while bits and not bits[-1]:
            bits.pop()
        result = 0
        while bits:
            result *= 2
            result += bits.pop()
        return result
