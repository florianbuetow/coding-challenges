# link: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        # O(n) time and space

        def findIntervals():
            intervals = []
            left = window = 0
            for right, n in enumerate(arr):
                window += n
                while window > target:
                    window -= arr[left]
                    left += 1
                if window == target:
                    intervals.append([left, right, right - left + 1])
            return intervals

        def helper(intervals):
            res = shortest = float('inf')
            left = 0
            for right in range(len(intervals)):
                while left < right and intervals[left][1] < intervals[right][0]:
                    shortest = min(shortest, intervals[left][2])
                    left += 1
                res = min(res, shortest + intervals[right][2])
            return res if res != float('inf') else -1

        return helper(findIntervals())
