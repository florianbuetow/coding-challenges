# link: https://leetcode.com/problems/reverse-string-prefix/


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # O(n) time and O(1) space
        s = list(s)
        for i in range(k // 2):
            s[i], s[k-1-i] = s[k-1-i], s[i]
        return ''.join(s)
