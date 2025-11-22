# O(n) time and O(1) space
# link: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result += min(n % 3, 3 - n % 3)
        return result
