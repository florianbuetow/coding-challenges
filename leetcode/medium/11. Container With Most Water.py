# O(n) time and O(1) space
# link: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result


        # O(n*n) time and O(1) space
        result = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                area = min(height[left], height[right]) * (right - left)
                result = max(result, area)
        return result
