# O(n*n) time and O(n) space
# link: https://leetcode.com/problems/champagne-tower/


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr_row = [poured]
        for row in range(query_row):
            next_row = [0]
            for col, amount in enumerate(curr_row):
                next_row.append(0)
                excess = max(0, (amount - 1.0) / 2.0)
                next_row[-1] += excess
                next_row[-2] += excess
            curr_row = next_row
        return min(1.0, curr_row[query_glass])
