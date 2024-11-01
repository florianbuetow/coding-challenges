class Solution:
    def scoreOfString(self, s: str) -> int:
        # O(n) time, O(1) space
        # link: https://leetcode.com/problems/score-of-a-string/
        result = 0
        for i in range(1, len(s)):
            c_cur = ord(s[i]) - ord('a')
            c_prv = ord(s[i-1]) - ord('a')
            result += abs(c_prv - c_cur)
        return result