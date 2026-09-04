# link: https://leetcode.com/problems/smallest-stable-index-i/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # O(n) time and space
        
        result = float('inf')
        def helper(idx, cur_max=0):
            if idx == len(nums): 
                return float('inf')
            
            nonlocal result
            cur_max = max(nums[idx], cur_max)
            cur_min = min(nums[idx], helper(idx + 1, cur_max))
            if cur_max - cur_min <= k: result = idx
            return cur_min

        helper(0)
        return result if result < len(nums) else -1
