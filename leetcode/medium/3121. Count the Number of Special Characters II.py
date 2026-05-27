# link: https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # O(n) time and space
        firstUpper = {}
        lastLower = {}

        for i, c in enumerate(word):
            if 'A' <= c <= 'Z':
                if c not in firstUpper:
                    firstUpper[c] = i
            else:
                lastLower[c] = i

        result = 0
        for cdn in lastLower:
            cup = cdn.upper()
            if cup in firstUpper:
                if lastLower[cdn] < firstUpper[cup]:
                    result += 1
        return result
