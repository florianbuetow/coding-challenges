# O(n) time and O(1) space
# link: https://leetcode.com/problems/minimum-penalty-for-a-shop

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty_open = penalty_closed = 0
        for c in customers:
            if c == 'Y': penalty_closed += 1

        result, penalty_min = 0, penalty_open + penalty_closed
        for hour, c in enumerate(customers, start=1):
            if c == 'Y': penalty_closed -= 1
            if c == 'N': penalty_open += 1
            penalty_cur = penalty_open + penalty_closed
            if penalty_cur < penalty_min:
                penalty_min = penalty_cur
                result = hour
        return result
