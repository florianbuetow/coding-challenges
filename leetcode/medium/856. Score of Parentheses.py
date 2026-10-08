class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # O(n) time and space
        tmp = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(tmp)
                stack.append(c)
                tmp = 0
            else:
                if stack[-1] == '(':
                    stack.pop()
                    tmp = 1
                else:
                    tmp = stack.pop() * 2
                    stack.pop()

                while stack and stack[-1] != '(':
                    tmp += stack.pop()

                stack.append(tmp)
                tmp = 0

        return stack[0]
