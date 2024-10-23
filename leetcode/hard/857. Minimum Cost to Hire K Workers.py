from heapq import heappush, heappop
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # O(n log n) time and O(n) space
        # idea: sort workers by wage/quality ratio ascending
        #       iterate through the workers by they wage/quality ratio
        #       maintain a list of k workers with the highest quality so far
        #       compute the cost of that group by multiplying their summed quality wiht the largest wage/quality ratio in the group
        #       the minimum of all these costs is the result
        ratio = [[wage[i] / quality[i], quality[i]] for i in range(len(quality))]
        ratio.sort()

        result, maxheap, sum_quality = float('inf'), [], 0
        for i in range(len(quality)):
            heapq.heappush(maxheap, -ratio[i][1]) # quality values are negative to give us a max heap
            sum_quality += ratio[i][1]
            while len(maxheap) > k:
                sum_quality += heapq.heappop(maxheap) # substract from the total quality from the group
            if len(maxheap) == k:
                result = min(result, sum_quality * ratio[i][0])
        return result