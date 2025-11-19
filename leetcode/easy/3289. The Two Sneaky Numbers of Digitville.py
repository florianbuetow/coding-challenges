# O(n) time and space
# link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            nums[i] += 1

        for i in range(len(nums)):
            n = abs(nums[i]) - 1
            if nums[n] < 0:
                duplicates.append(n)
            else:
                nums[n] *= -1
        return duplicates
