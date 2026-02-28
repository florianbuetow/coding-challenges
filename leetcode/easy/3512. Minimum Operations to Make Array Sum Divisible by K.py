# link: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # O(n) time and O(1) space
        return sum(nums) % k
