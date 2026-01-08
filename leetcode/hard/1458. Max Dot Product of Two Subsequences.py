# O(n*m) time and O(m) space
# link: https://leetcode.com/problems/max-dot-product-of-two-subsequences

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        prev = [float('-inf')] * (len(nums2) + 1)
        curr = [float('-inf')] * (len(nums2) + 1)
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                product = nums1[i - 1] * nums2[j - 1]
                curr[j] = max(
                    prev[j],
                    curr[j - 1],
                    product,
                    product + max(0, prev[j - 1])
                )
            curr, prev = prev, curr
        return prev[len(nums2)]
