# link: https://leetcode.com/problems/partition-array-according-to-given-pivot/


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # O(n) time and space
        partitions = [[],[],[]]
        for n in nums:
            if n < pivot: partition = 0
            if n == pivot: partition = 1
            if n > pivot: partition = 2
            partitions[partition].append(n)
        index = 0
        for partition in range(3):
            for n in partitions[partition]:
                nums[index] = n
                index += 1
        return nums
