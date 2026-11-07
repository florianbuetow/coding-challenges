# link: https://leetcode.com/problems/create-grid-with-exactly-one-path/

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # O(n * m) time and space
        result = []
        for _ in range(m):
            if result:
                result.append('#' * (n-1) + '.')
            else:
                result.append('.' * n)
        return result
