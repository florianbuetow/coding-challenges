# link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # O(n) time and O(1) space
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
