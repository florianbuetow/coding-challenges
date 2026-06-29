# link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # O(n*m) time and O(1) space
        counter = 0
        for p in patterns:
            if p in word:
                counter += 1
        return counter
