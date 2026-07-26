# O(2^n) time and O(n) space
# link: https://www.hackerrank.com/challenges/the-power-sum

import functools

def powerSum(X, N):
    @functools.cache
    def helper(n, rest):
        if rest == 0: return 1
        if rest < n ** N: return 0
        return helper(n + 1, rest - n ** N) + helper(n + 1, rest)
    return helper(1, X)
