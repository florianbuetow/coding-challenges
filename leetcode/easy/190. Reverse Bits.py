# O(log n) time and space
# link: https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0] * 32
        idx = len(bits)
        while n:
            idx -= 1
            bits[idx] = n % 2
            n //= 2
        for exp, bit in enumerate(bits):
            n += bit * 2**exp
        return n
