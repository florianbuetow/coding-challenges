# link: https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        xor  = 0
        zeros = True
        for n in nums:
            xor ^= n
            zeros &= (n == 0)
        if xor: return len(nums)
        if zeros: return 0
        return len(nums) - 1
