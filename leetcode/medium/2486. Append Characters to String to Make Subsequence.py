 class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # O(n) time and O(1) space, n = len(s)
        index = 0
        for c in s:
            if c == t[index]:
                index += 1
            if index == len(t): return 0
        return len(t) - index