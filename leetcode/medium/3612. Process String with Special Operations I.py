# link: https://leetcode.com/problems/process-string-with-special-operations-i/

class Solution:
    def processStr(self, s: str) -> str:
        # O(2^n) time and space
        result = []
        for c in s:
            if c == '*':
                if result: result.pop()
            elif c == '#':
                result += result
            elif c == '%':
                result = result[::-1]
            else:
                result.append(c)
        result = "".join(result)
        return result
