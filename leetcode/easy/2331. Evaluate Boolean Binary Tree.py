# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # O(n) time and space        
        def helper(node) -> bool:
            if node.left or node.right:
                if node.val == 2: return helper(node.left) or helper(node.right)
                if node.val == 3: return helper(node.left) and helper(node.right)
            return node.val            
        return helper(root)