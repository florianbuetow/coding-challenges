# link: https://leetcode.com/problems/smallest-pair-with-different-frequencies/

from collections import defaultdict

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        # O(n*n) time and O(n) space
        frequencies = defaultdict(int)
        for n in nums:
            frequencies[n] += 1
        inverted_frequencies = defaultdict(list)

        nums = sorted(frequencies.keys())
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x, y = nums[i], nums[j]
                if frequencies[x] != frequencies[y]:
                    return [x, y]
        return [-1, -1]
