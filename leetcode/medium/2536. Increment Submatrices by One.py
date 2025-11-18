# O(m + n*n) time and O(n*n) space, m = len(queries)
# link: https://leetcode.com/problems/increment-submatrices-by-one

class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        change = []
        for _ in range(n):
            change.append([0]*n)

        for r1, c1, r2, c2 in queries:
            change[r1  ][c1  ] += 1
            if r2 + 1 < n: change[r2+1][c1  ] -= 1
            if c2 + 1 < n: change[r1  ][c2+1] -= 1
            if max(r2, c2) + 1 < n: change[r2+1][c2+1] += 1

        matrix = change
        for r in range(n):
            for c in range(n):
                matrix[r][c] = change[r][c] # just for clarity
                if r > 0: matrix[r][c] += matrix[r-1][c]
                if c > 0: matrix[r][c] += matrix[r][c-1]
                if min(r, c) > 0: matrix[r][c] -= matrix[r-1][c-1]
        return matrix
