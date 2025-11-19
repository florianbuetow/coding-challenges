# O(n) time and O(1) space
# link: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1: return True
        counter = i = 0
        while i+k+1 < len(nums):
            if nums[i] < nums[i+1] and nums[i+k] < nums[i+k+1]:
                counter += 1
                if counter == k - 1:
                    return True
            else:
                counter = 0
            i += 1
        return False
