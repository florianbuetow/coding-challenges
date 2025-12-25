from heapq import heapify, heappop

# O(n + k log n) time and O(1) space
# link: https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        for i in range(len(happiness)):
            happiness[i] *= -1
        heapify(happiness)

        result = decrease = 0
        while k and -happiness[0] > decrease:
            happy = -heappop(happiness) - decrease
            result += happy
            decrease += 1
            k -= 1

        for i in range(len(happiness)):
            happy = happiness[i] - decrease
            result += max(0, happy)
        return result
