# link: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # O(n+m) time and O(1) space
        length = width = length_min = width_min = 300005
        n, m = len(landStartTime), len(waterStartTime)

        for i in range(n):
            length = min(length, landStartTime[i] + landDuration[i])
        for i in range(m):
            width = min(width, waterStartTime[i] + waterDuration[i])
            length_min = min(length_min, max(waterStartTime[i], length) + waterDuration[i])
        for i in range(n):
            width_min = min(width_min, max(landStartTime[i], width) + landDuration[i])
        return min(width_min, length_min)
