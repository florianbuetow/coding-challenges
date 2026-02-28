# link: https://leetcode.com/problems/keep-multiplying-found-values-by-two/


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # O(n) time and O(1) space
        nums = set(nums)
        while original in nums:
            original *= 2
        return original
