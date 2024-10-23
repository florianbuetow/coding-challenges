from heapq import heapify, heappop
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # O(n + k log n) time and O(1) space
        for i in range(len(happiness)):
            happiness[i] *= -1
        heapify(happiness)

        result = decrease = 0
        for _ in range(k):
            result += max(0, -heappop(happiness) - decrease)
            decrease += 1
        return result