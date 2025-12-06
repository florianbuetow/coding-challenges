# O(n) time and space, n = max(nums) - min(nums)
# link: https://leetcode.com/problems/find-missing-elements/

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        nums = set(nums)
        for n in range(min(nums)+1, max(nums)):
            if n not in nums:
                result.append(n)
        return result
