# O(n*n) time and O(m) space, n = len(b) / len(a), m = len(b)
# link: https://leetcode.com/problems/repeated-string-match/


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        c = ''
        repeats = 0
        while len(c) <= len(b) * 2 or repeats <= 3:
            if b in c: return repeats
            repeats += 1
            c += a
        return -1
