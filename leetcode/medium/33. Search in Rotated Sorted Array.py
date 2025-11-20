# O(log n) time and O(1) space
# link: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMinimumIndex():
            boundary_index = 0
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                val = nums[mid]
                if val <= nums[-1]:
                    boundary_index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return boundary_index

        offset = findMinimumIndex()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            idx = (offset + mid) % len(nums)
            val = nums[idx]
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return idx
        return -1
