class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # O(n) time and space
        stack = []
        remove = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        while stack:
            remove.add(stack.pop())
        return "".join([c for i, c in enumerate(s) if i not in remove])
