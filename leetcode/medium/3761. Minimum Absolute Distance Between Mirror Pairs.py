# link: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # O(n) time and space
        def rev(n):
            res = 0
            digits = list(str(n))
            while digits:
                res *= 10
                res += int(digits.pop())
            return res

        result = float('inf')
        index = {}
        for i, n in enumerate(nums):
            if n in index:
                result = min(
                    result,
                    i - index[n]
                )
            index[rev(n)] = i
        if result == float('inf'):
            result = -1
        return result
