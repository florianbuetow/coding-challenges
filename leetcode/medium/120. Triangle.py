# O(n*n) time and O(n) space, where n is the height and width of the triangular array
# link: https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        path_sums = []
        for row in triangle:
            if not path_sums:
                path_sums = row
            else:
                tmp = []
                for i, val in enumerate(row):
                    min_path_sum_parent = float('inf')
                    if i > 0:
                        min_path_sum_parent = min(min_path_sum_parent, path_sums[i-1])
                    if i < len(path_sums):
                        min_path_sum_parent = min(min_path_sum_parent, path_sums[i])
                    tmp.append(val + min_path_sum_parent)
                path_sums = tmp
        return min(path_sums)
