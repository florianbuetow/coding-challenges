class Solution:
    def checkValidString(self, s: str) -> bool:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/valid-parenthesis-string/
        left, right = 0, len(s) - 1
        count_open = count_close = 0
        while left < len(s) and right >= 0:
            if s[left] in '(*':
                count_open += 1
            else:
                count_open -= 1

            if s[right] in '*)':
                count_close += 1
            else:
                count_close -= 1

            if count_open < 0: return False
            if count_close < 0: return False
            left += 1
            right -= 1
        return True
