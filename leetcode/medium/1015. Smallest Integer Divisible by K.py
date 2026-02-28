# link: https://leetcode.com/problems/smallest-integer-divisible-by-k


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # O(n) time and O(1) space
        rest = 0
        for length in range(k):
            rest = (rest * 10 + 1) % k
            if rest == 0:
                return length + 1
        return -1
