from heapq import heappush, heappop
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        # Idea: find the four smallest and four largest elements
        #       then compute the pairwise min difference between them
        if len(nums) < 5:
            return 0
        min_heap, max_heap = [], []
        for n in nums:  # O(n)
            heappush(min_heap, -n)
            heappush(max_heap, n)
            if len(min_heap) >= 5:  # O(1)
                heappop(min_heap)
                heappop(max_heap)

        result = float('inf')
        min_heap.sort(reverse=True) # O(1)
        max_heap.sort() # O(1)
        for a, b in zip(max_heap, min_heap): # O(1) because length == 4
            result = min(result, a + b) # + because values in min_heap are negative
        return result
