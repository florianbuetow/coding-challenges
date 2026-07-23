# link: https://leetcode.com/problems/number-of-unique-xor-triplets-i/

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # O(1) time and space
        n = len(nums)
        if n >= 3:
            n = 2 ** n.bit_length()
        return n
