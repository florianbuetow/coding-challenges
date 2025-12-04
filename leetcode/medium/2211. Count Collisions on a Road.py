# O(n) time and space
# link: https://leetcode.com/problems/count-collisions-on-a-road

class Solution:
    def countCollisions(self, directions: str) -> int:
        result = 0
        stack = ['L']
        for d in directions:
            if d == 'R':
                stack.append('R')
            elif d == 'S':
                while stack[-1] == 'R':
                    result += 1
                    stack.pop()
                stack.append('S')
            elif d == 'L':
                if stack[-1] == 'S':
                    result += 1
                elif stack[-1] == 'R':
                    stack.pop()
                    result += 2
                    while stack[-1] == 'R':
                        result += 1
                        stack.pop()
                    stack.append('S')
        return result
