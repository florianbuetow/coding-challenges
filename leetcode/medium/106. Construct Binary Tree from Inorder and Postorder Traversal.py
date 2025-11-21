# O(n) time and O(n) space
# link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # O(n) time and space
        inorderIndex = {val: i for i, val in enumerate(inorder)}
        def helper(left, right):
            if left > right:
                return None
            val = postorder.pop()
            node = TreeNode(val)
            mid = inorderIndex[val]
            node.right = helper(mid + 1, right)
            node.left = helper(left, mid - 1)
            return node
        return helper(0, len(inorder)-1)
