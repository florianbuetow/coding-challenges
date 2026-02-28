# link: https://leetcode.com/problems/vowels-game-in-a-string/


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # O(n) time and O(1) space
        for c in s:
            if c in "aeiou":
                return True
        return False
