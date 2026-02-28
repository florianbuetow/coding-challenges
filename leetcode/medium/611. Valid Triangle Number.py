# link: https://leetcode.com/problems/valid-triangle-number/


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        result = 0
        nums.sort()
        for index in range(len(nums)-1,-1,-1):
            left, right = 0, index - 1
            while left < right:
                a, b, c = nums[left], nums[right], nums[index]
                if a + b > c:
                    result += (right - left)
                    right -=1
                else:
                    left += 1
        return result
