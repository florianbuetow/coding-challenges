from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(n) time and space, n = len(nums)
        # link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1        
        return [n for n, count in counter.items() if count == 2]