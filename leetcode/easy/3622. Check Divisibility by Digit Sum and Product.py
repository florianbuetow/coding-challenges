# link: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # O(log n) time and O(1) space
        def sumDigits(n):
            summ = 0
            while n:
                summ += n % 10
                n //= 10
            return summ

        def mulDigits(n):
            prod = 1
            while n:
                prod *= n % 10
                n //= 10
            return prod

        d = sumDigits(n) + mulDigits(n)
        return n % d == 0
