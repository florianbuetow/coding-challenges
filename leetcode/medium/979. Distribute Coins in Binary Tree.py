from typing import Optional


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # O(n) time and space
        # link: https://leetcode.com/problems/distribute-coins-in-binary-tree/
        result = 0
        def helper(node):
            if node:
                nonlocal result
                left_coins = helper(node.left)
                right_coins = helper(node.right)
                result += abs(left_coins) + abs(right_coins)
                return left_coins + right_coins + (node.val - 1)
            return 0
        helper(root)
        return result