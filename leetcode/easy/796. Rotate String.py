# link: https://leetcode.com/problems/rotate-string/


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # O(n) time and O(1) space
        l = len(s)
        if l == len(goal):
            for i in range(l):
                prefix, postfix = s[i:], s[:i]
                if prefix + postfix == goal:
                    return True
        return False
