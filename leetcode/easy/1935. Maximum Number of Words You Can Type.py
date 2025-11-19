# O(n) time and O(1) space
# link: https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0
        skip = False
        for i, c in enumerate(text):
            if c in brokenLetters:
                skip = True
            if c == ' ' or i == len(text) - 1:
                if not skip:
                    result +=1
                skip = False
        return result
