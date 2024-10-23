# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # O(n) time and space
        def helper(node, isLeftChild):
            if not node.left and not node.right:
                return [0, node.val][isLeftChild]
            result = 0
            if node.right: result += helper(node.right, False)
            if node.left: result += helper(node.left, True)
            return result
        return helper(root, False)