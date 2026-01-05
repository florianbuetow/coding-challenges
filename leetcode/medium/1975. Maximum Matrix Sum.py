# O(n*n) time and O(1) space
# link: https://leetcode.com/problems/maximum-matrix-sum

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = count = 0
        min_n = float('inf')
        for row in matrix:
            for cur_n in row:
                if cur_n < 0: count += 1
                min_n = min(min_n, abs(cur_n))
                result += abs(cur_n)
        if count % 2 != 0:
            result -= 2 * min_n
        return result
