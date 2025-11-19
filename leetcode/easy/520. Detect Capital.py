# O(n) time and O(1) space, n = len(word)
# link: https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        firstIsUpper = restIsUpper = None
        for i in range(len(word)):
            currIsUpper = word[i].upper() == word[i]
            if i == 0:
                firstIsUpper = currIsUpper
            elif i == 1:
                restIsUpper = currIsUpper
                if restIsUpper and not firstIsUpper:
                    return False
            elif currIsUpper != restIsUpper:
                return False
        return True
