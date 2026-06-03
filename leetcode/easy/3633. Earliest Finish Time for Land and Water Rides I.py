# link: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/


class Solution:
    def earliestFinishTime(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        # O(n+m) time and O(1) space
        result = float('inf')
        minEnd = float('inf')
        for i in range(len(a)): minEnd = min(minEnd, a[i] + b[i])
        for i in range(len(c)): result = min(result, d[i] + max(minEnd, c[i]))
        minEnd = float('inf')
        for i in range(len(c)): minEnd = min(minEnd, c[i] + d[i])
        for i in range(len(a)): result = min(result, b[i] + max(minEnd, a[i]))
        return result
