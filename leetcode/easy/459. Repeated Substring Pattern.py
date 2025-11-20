# O(n*n) time and O(n) space
# link: https://leetcode.com/problems/repeated-substring-pattern/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(1, l):
            if l % i == 0:
                prefix = s[:i]
                if prefix * (l // i) == s:
                    return True
        return False
