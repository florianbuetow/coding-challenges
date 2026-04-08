# link: https://leetcode.com/problems/xor-after-range-multiplication-queries-i

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # O(n*n*m) time and O(n) space, n = len(nums), m = len(querries)
        for q in queries:
            l, r, k, v = q
            for i in range(l, r+1, k):
                nums[i] *= v
                nums[i] %= 10**9 + 7
        result = 0
        for n in nums:
            result ^= n
        return result
