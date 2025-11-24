# O(n) time and O(n) space
# link: https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        n = 0
        for bit in nums:
            n = n * 2 + bit
            result.append(n % 5 == 0)
        return result
