# O(n log n) time and O(n) space
# link: https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, mid, right):
            tmp = []
            j = mid
            for i in range(left, mid):
                while j < right and nums[j] <= nums[i]:
                    tmp.append(nums[j])
                    j += 1
                tmp.append(nums[i])
            for i, n in enumerate(tmp):
                nums[left + i] = n

        def mergeSort(left, right):
            if left + 1 < right:
                mid = (left + right) // 2
                mergeSort(left, mid)
                mergeSort(mid, right)
                merge(left, mid, right)
            return nums

        return mergeSort(0, len(nums))
