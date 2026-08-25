# link: https://leetcode.com/problems/smallest-missing-multiple-of-k/

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # O(n) time and space
        nums = set(nums)
        result = k
        while result in nums:
            result += k
        return result
