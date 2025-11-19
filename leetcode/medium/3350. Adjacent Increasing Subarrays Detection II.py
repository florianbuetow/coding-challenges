# O(n) time and O(1) space
# link: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        result = 0
        prev_count, count = 0, 1
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                prev_count = count
                count = 0
            count += 1
            result = max(result, count // 2)
            result = max(result, min(count, prev_count))
        return result
