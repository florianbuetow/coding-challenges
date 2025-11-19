# O(n) time and space
# link: https://leetcode.com/problems/license-key-formatting/


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if c == '-': continue
            if not result or len(result[-1]) >= k:
                result.append([])
            result[-1].append(c.upper())

        result.reverse()
        for i in range(len(result)):
            result[i] = ''.join(result[i][::-1])
        return '-'.join(result)
