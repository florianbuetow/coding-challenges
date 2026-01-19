# O(n^3) time and O(n) space, n = cells in the matrix
# link: https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold

from itertools import accumulate


class Solution:

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        prefix_sums = [[0] * (cols + 1)]
        for row in mat:
            prefix_sums.append([0] + list(accumulate(row)))
            for col in range(cols + 1):
                prefix_sums[-1][col] += prefix_sums[-2][col]

        result, left, right = 0, 1, min(rows, cols)
        while left <= right:
            mid = (left + right) // 2
            for row in range(mid, rows + 1):
                found = False
                for col in range(mid, cols + 1):
                    tmp = prefix_sums[row][col]
                    tmp -= prefix_sums[row - mid][col]
                    tmp -= prefix_sums[row][col - mid]
                    tmp += prefix_sums[row - mid][col - mid]
                    if tmp <= threshold:
                        found = True
                        break
                if found:
                    break
            if not found:
                right = mid - 1
                continue
            result = max(result, mid)
            left = mid + 1
        return result
