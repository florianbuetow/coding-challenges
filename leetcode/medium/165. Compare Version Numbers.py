# O(n+m) time and O(1) space, n = len(version1), m = len(version2)
# link: https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        def getRevisionValue(idx, s):
            value = 0
            while idx < len(s) and s[idx] != '.':
                value *= 10
                value += int(s[idx])
                idx += 1
            return value, idx + 1

        i1 = i2 = 0
        while i1 < len(version1) or i2 < len(version2):
            val1, i1 = getRevisionValue(i1, version1)
            val2, i2 = getRevisionValue(i2, version2)
            if val1 < val2: return -1
            if val1 > val2: return +1
        return 0
