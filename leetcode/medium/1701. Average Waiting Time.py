class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/average-waiting-time/
        avg_wait = t_free = 0
        for t_order, t_cooking in customers:
            cus_wait = max(0, t_free - t_order ) + t_cooking
            avg_wait += cus_wait / len(customers)
            t_free = max(t_free, t_order) + t_cooking
        return avg_wait