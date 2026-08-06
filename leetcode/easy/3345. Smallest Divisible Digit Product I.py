# link: https://leetcode.com/problems/smallest-divisible-digit-product-i/


from functools import reduce
from operator import mul


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # O(log n) time and space
        def digitProduct(n):
            return reduce(mul, map(int, str(n)), 1)

        while digitProduct(n) % t != 0:
            n += 1
        return n
