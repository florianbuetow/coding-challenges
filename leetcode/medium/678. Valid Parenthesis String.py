class Solution:
    def checkValidString(self, s: str) -> bool:
        # O(n) time and space, n = len(s)
        stack_open = []
        stack_star = []
        for i, c in enumerate(s):
            if c == '(':  stack_open.append(i)
            if c == '*':  stack_star.append(i)
            if c == ')':
                if stack_open:
                    stack_open.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
        while stack_open and stack_star:
            i = stack_open.pop()
            j = stack_star.pop()
            if i > j: return False
        return len(stack_open) == 0