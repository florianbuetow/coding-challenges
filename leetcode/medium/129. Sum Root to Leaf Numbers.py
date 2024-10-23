# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # O(n) time and O(h) space, n = number of nodes in the tree, h = height of the tree
        def helper(node, summ):
            summ *= 10
            summ += node.val
            if node.left or node.right:
                result = 0
                if node.left: result += helper(node.left, summ)
                if node.right: result += helper(node.right, summ)
                return result
            return summ
        return helper(root, 0)