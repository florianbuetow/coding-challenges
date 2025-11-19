# O(n log n) time and O(1) space
# link: https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        curr_min_val = nums[0] - k
        curr_max_val = nums[0] + k
        for n in nums:
            curr_min_val = max(curr_min_val, n - k)
            curr_max_val = n + k
            if curr_min_val > curr_max_val:
                continue
            result += 1
            curr_min_val += 1
        return result
