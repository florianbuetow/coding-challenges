# O(n) time and space
# link: https://leetcode.com/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        squares = set()
        for i in range(1, n + 1):
            squares.add(i * i)

        result = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a ** 2 + b ** 2 in squares:
                    result += 1
        return result
