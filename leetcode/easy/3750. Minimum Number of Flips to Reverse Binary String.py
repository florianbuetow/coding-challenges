# O(log n) time and space
# link: https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution:
    def minimumFlips(self, n: int) -> int:
        def getBits(n):
            bits = []
            while n:
                bits.append(n%2)
                n//=2
            return bits

        result = 0
        bits = getBits(n)
        for i in range(len(bits)):
            if bits[i] != bits[-(i+1)]:
                result += 1
        return result
