# O(log n) time and O(1) space
# link: https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2

            val_left = arr[mid-1] if mid > 0 else -float('inf')
            val_mid = arr[mid+0]
            val_right = arr[mid+1] if mid < len(arr) else -float('inf')

            if val_left < val_mid and val_mid < val_right:
                left = mid + 1
            elif val_left > val_mid and val_mid > val_right:
                right = mid - 1
            else:
                return mid
