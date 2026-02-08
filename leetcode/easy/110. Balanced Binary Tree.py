# O(n) time and space
# link: https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_height_balanced = True

        def get_height(node):
            if not node:
                return 0
            l = get_height(node.left)
            r = get_height(node.right)
            if abs(l - r) >= 2:
                nonlocal is_height_balanced
                is_height_balanced = False
            return max(l, r) + 1

        get_height(root)
        return is_height_balanced
