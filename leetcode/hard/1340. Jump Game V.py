# link: https://leetcode.com/problems/jump-game-v/

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # O(n * d) time and O(n) space
        @cache
        def helper(i):
            res = 1
            for j in range(i + 1, min(i + d, len(arr) - 1) + 1):
                if arr[j] >= arr[i]: break
                res = max(res, 1 + helper(j))
            for j in range(i - 1, max(0, i - d) - 1, -1):
                if arr[j] >= arr[i]: break
                res = max(res, 1 + helper(j))
            return res

        result = 0
        for i in range(len(arr)):
            result = max(result, helper(i))
        return result
