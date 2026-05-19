# link: https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # O(n) time and O(1) space
        i = 0
        for n in nums2:
            while nums1[i] < n:
                i += 1
                if i == len(nums1): return -1
            if nums1[i] == n:
                return n
        return -1
