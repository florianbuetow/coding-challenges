# link: https://leetcode.com/problems/smallest-stable-index-ii/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # O(n) time and space
        stack = [len(nums)-1]
        for idx in range(len(nums)-1,-1,-1):
            if nums[idx] < nums[stack[-1]]:
                stack.append(idx)
        cur_max = 0
        for idx, n  in enumerate(nums):
            cur_max = max(n, cur_max)
            if stack[-1] < idx:
                stack.pop()
            if stack:
                cur_score = cur_max - nums[stack[-1]]
                if cur_score <= k:
                    return idx
        return -1
