# link: https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # O(n) time and space, n = len(nums)
        lookup = defaultdict(int)
        counts = defaultdict(int)
        for i, n in enumerate(nums):
            lookup[n] += i
            counts[n] += 1

        result = [0] * len(nums)
        for i, n in enumerate(nums):
            result[i] = lookup[n] - i * counts[n]
            lookup[n] -= 2 * i
            counts[n] -= 2
        return result
