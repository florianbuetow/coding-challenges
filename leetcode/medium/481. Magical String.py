# O(n) time and space
# link: https://leetcode.com/problems/magical-string/

class Solution:
    def magicalString(self, n: int) -> int:
        stack = [1, 2, 2]
        idx = len(stack) - 1
        while len(stack) < n:
            num = stack[-1]
            for _ in range(stack[idx]):
                stack.append(3 - num)
            idx += 1

        result = 0
        for i in range(n):
            if stack[i] == 1:
                result += 1
        return result
