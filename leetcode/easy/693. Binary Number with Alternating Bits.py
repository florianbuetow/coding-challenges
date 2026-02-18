# O(log n) time and O(1) space
# link: https://leetcode.com/problems/binary-number-with-alternating-bits/


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = (n + 1) % 2
        while n and n % 2 != last_bit:
            last_bit = n % 2
            n //= 2
        return n == 0
