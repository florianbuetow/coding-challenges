# link: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # O(n log n) time and O(1) space
        cost.sort(reverse=True) # in-place sorting
        total_min_cost = 0
        for i in range(len(cost)):
            if i%3 in [0, 1]:
                total_min_cost +=cost[i]
        return total_min_cost
