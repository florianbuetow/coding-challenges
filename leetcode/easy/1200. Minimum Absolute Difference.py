# O(n log n) time and O(n) space
# link: https://leetcode.com/problems/minimum-absolute-difference/

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_dist = float('inf')
        for i in range(len(arr)-1):
            dist = arr[i+1] - arr[i]
            min_dist = min(min_dist, dist)

        result = []
        for i in range(len(arr)-1):
            dist = arr[i+1] - arr[i]
            if dist == min_dist:
                result.append([arr[i], arr[i+1]])
        return result
