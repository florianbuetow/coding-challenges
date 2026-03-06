# link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # O(n) time and O(1) space
        foundOnes = False
        idx = 0
        while idx < len(s) and s[idx] == '0':
            idx += 1
        while idx < len(s) and s[idx] == '1':
            foundOnes = True
            idx += 1
        while idx < len(s) and s[idx] == '0':
            idx += 1
        if not foundOnes: return False
        if foundOnes and idx < len(s): return False
        return True
