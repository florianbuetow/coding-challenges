# O(n log n) time and O(n) space
# link: https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda e: e[1])
        intervals.sort(key=lambda e: e[0])
        prev_interval = intervals[0]
        for curr_interval in intervals:
            # case 1 non overlapping (potentially touching)
            if prev_interval[1] + 1 <= curr_interval[0]:
                result.append(prev_interval)
                prev_interval = curr_interval
            else:
                # case 2: overlapping
                prev_interval[1] = max(prev_interval[1], curr_interval[1])
        if prev_interval:
            result.append(prev_interval)
        return result
