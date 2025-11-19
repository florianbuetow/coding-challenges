# O(n) time and O(n) space
# link: https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0
        for word in text.split(' '):
            if any(c for c in word if c in brokenLetters):
                continue
            result += 1
        return result
