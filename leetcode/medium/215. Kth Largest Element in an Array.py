# O(k log n) time and O(1) space
# link: https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)

        result = -nums[0]
        while nums and k:
            result = -heappop(nums)
            k -= 1
        return result
