class Solution:
    def reverseParentheses(self, s: str) -> str:
        #O(n) time and space
        def getSubstrings(s):
            substrings = defaultdict(int)
            stack = []
            for right in range(len(s)):
                if s[right] == '(':
                    stack.append(right)
                elif s[right] == ')':
                    left = stack.pop()
                    substrings[right] = left
                    substrings[left] = right
            return substrings

        substrings = getSubstrings(s)
        result = []
        index, direction = 0, 1
        while index < len(s):
            if s[index] in '()':
                index = substrings[index]
                direction = -direction
            else:
                result.append(s[index])
            index += direction

        return ''.join(result)