class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        if k > 1:
            product, left = 1, 0
            for right, num in enumerate(nums):
                product *= num
                while product >= k:
                    product //= nums[left]
                    left += 1
                result += right - left + 1
        return result