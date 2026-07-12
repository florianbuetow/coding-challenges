# link: https://leetcode.com/problems/rank-transform-of-an-array/


from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # O(n log n) time and O(n) space
        rank = {n: i for i, n in enumerate(sorted(set(arr)), start=1)}
        return [rank[n] for n in arr]
