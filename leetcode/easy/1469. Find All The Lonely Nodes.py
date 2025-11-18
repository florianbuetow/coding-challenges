# O(n) time and O(h) space, n = number of nodes, h = height of tree
# link: https://leetcode.com/problems/find-all-the-lonely-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, singleChild, result):
            if singleChild: result.append(node.val)
            singleChild = False
            if node.left is None and node.right: singleChild = True
            if node.left and node.right is None: singleChild = True
            if node.left: helper(node.left, singleChild, result)
            if node.right: helper(node.right, singleChild, result)
            return result
        return helper(root, False, [])