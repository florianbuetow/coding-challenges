# link: https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # O(n) time and O(1) space
        result = float('inf')
        for i, n in enumerate(nums):
            if n == target:
                result = min(result, abs(i - start))
        return result
