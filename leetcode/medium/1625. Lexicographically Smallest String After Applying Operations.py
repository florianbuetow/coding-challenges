# O(n*n) time and O(n*n) space
# link: https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        result = s
        visited = set()
        stack = [s]
        while stack:
            s = stack.pop()
            if s in visited: continue
            visited.add(s)
            result = min(result, s)
            t = s[b:] + s[:b]
            if t not in visited: stack.append(t)
            t = "".join([str((int(digit) + a*[0,1][i%2]) % 10) for i, digit in enumerate(s)])
            if t not in visited: stack.append(t)
        return result
