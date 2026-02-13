# O(n) time and space
# link: https://leetcode.com/problems/longest-balanced-substring-ii/

from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        def helper(x, y, z):
            res = 0
            i = 0
            while i < len(s):
                if s[i] == z:
                    i += 1
                    continue
                start = j = i
                balance = 0
                prev = {0: start}
                while j < len(s) and s[j] != z:
                    balance += [-1, 1][s[j] == x]
                    if balance not in prev:
                        prev[balance] = j + 1
                    else:
                        res = max(res, j + 1 - prev[balance])
                    j += 1
                i = j
            return res

        result = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            result = max(result, j - i)
            i = j

        result = max(
            result,
            helper('a', 'b', 'c'),
            helper('a', 'c', 'b'),
            helper('b', 'c', 'a')
        )

        count = defaultdict(int)
        mp = {(0, 0): -1}
        for i in range(len(s)):
            count[s[i]] += 1
            key = (count['a'] - count['b'], count['a'] - count['c'])
            if key in mp:
                result = max(result, i - mp[key])
            else:
                mp[key] = i
        return result
