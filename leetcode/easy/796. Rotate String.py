# O(n*n) time and O(n) space
# link: https://leetcode.com/problems/rotate-string/


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = len(s)
        if l == len(goal):
            for i in range(l):
                prefix, postfix = s[i:], s[:i]
                if prefix + postfix == goal:
                    return True
        return False
