# link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/


from math import sqrt

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # O(n) time and O(1) space
        def count_bits(n):
            bits = 0
            while n > 0:
                bits += n % 2
                n = n // 2
            return bits

        def is_prime(n):
            if n == 2: return True
            if n % 2 == 0: return False
            if n < 2: return False
            for divisor in range(3, int(sqrt(n)) + 1):
                if n % divisor == 0:
                    return False
            return True

        result = 0
        for n in range(left, right + 1):
            result += [0, 1][is_prime(count_bits(n))]
        return result
