# link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        # O(n) time and O(1) space
        mini, minn = 0, min(nums)
        if nums[-1] == minn:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] != minn: break
                mini = i
        else:
            for i, n in enumerate(nums):
                if n == minn:
                    mini = i
                    break
        prev = mini
        for curr in range(mini, mini + len(nums)):
            curr = curr % len(nums)
            if nums[prev] > nums[curr]: return False
            prev = curr
        return True
