# link: https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # O(n) time and O(1) space
        if min(nums1) % 2: return True
        return not any(n % 2 for n in nums1)
