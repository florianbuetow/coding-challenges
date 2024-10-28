from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
        index = 0
        def helper(minValue, maxValue):
            nonlocal index
            if index < len(preorder):
                value = preorder[index]
                if value < minValue: return
                if value > maxValue: return
                index += 1
                helper(minValue, value)
                helper(value, maxValue)
        helper(-float('inf'), float('inf'))
        return index >= len(preorder)