# link: https://leetcode.com/problems/construct-uniform-parity-array-i/

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # O(n) time and O(1) space
        all_odd = all_even = True
        first_odd = float('inf')
        for idx, n in enumerate(nums1):
            if n % 2 == 0:
                all_odd = False
            else:
                all_evel = False
                first_odd = min(idx, first_odd)
        if all_odd or all_even: return True
        return first_odd == 0
