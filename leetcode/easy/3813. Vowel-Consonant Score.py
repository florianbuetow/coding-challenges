# link: https://leetcode.com/problems/vowel-consonant-score/

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        # O(n) time and O(1) space
        score = 0
        v = c = 0
        for char in s:
            if char in 'aeiou':
                v += 1
            elif not char.isnumeric() and char.isalpha():
                c += 1
        if c > 0:
            score  = math.floor(v / c)
        return score
