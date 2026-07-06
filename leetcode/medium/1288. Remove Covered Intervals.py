# link: https://leetcode.com/problems/remove-covered-intervals/


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # O(n log n) time and O(1) space
        intervals.sort(key=lambda e: e[1])
        intervals.sort(key=lambda e: e[0])

        def contains(interval_a, interval_b):
            return interval_b[0] >= interval_a[0] and interval_b[1] <= interval_a[1]

        left = 0
        result = len(intervals)
        for right in range(1, len(intervals)):
            if contains(intervals[left], intervals[right]):
                result -= 1
                continue
            if contains(intervals[right], intervals[left]):
                result -= 1
            left = right
        return result
