# link: https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # O(n) time and O(1) space
        letters = [0] * 26
        for c in word:
            if 'a' <= c <= 'z': letters[ord(c) - ord('a')] |= 1
            if 'A' <= c <= 'Z': letters[ord(c) - ord('A')] |= 2
        result = 0
        for c in word:
            if 'a' <= c <= 'z': pos = ord(c) - ord('a')
            if 'A' <= c <= 'Z': pos = ord(c) - ord('A')
            if letters[pos] == 3:
                result += 1
                letters[pos] = -1
        return result
