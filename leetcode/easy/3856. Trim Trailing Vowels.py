# link: https://leetcode.com/problems/trim-trailing-vowels/

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        # O(n) time and space
        for idx in range(len(s)-1,-1,-1):
            c = s[idx]
            if c not in "aeiou":
                return s[:idx+1]
        return ""
