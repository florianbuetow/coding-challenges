# link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        maxvals = []
        for n in nums:
            maxvals.append(n - 1)
            maxvals.sort(reverse=True)
            if len(maxvals) > 2:
                maxvals.pop()
        return maxvals[0] * maxvals[1]
