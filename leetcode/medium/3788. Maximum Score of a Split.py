# O(n) time and space
# link: https://leetcode.com/problems/maximum-score-of-a-split

class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        suffix_min = []
        for i in range(len(nums)-1,0,-1):
            curr = nums[i]
            prev = curr if not suffix_min else suffix_min[-1]
            suffix_min.append(min(prev, curr))
        suffix_min.reverse()

        result = -float('inf')
        prefix_sum = 0
        for i in range(len(nums)-1):
            prefix_sum += nums[i]
            score = prefix_sum - suffix_min[i]
            result = max(result, score)
        return result
