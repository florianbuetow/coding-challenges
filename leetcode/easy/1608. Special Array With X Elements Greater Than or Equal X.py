class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # O(n) time and space
        # Idea: The result x must be in the range [1, len(n)]
        #       1. Count how many numbers are larger for any possible x
        #       2. Then use postfix sum to find a match

        n = len(nums)
        count_gte = [0] * (n + 1)
        for m in nums:
            index = min(n, m)
            count_gte[index] += 1

        total_gte = 0
        for x in range(n,0,-1):
            total_gte += count_gte[x]
            if x == total_gte: return x
        return -1
