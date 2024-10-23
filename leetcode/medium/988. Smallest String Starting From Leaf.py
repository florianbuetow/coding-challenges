# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # O(n*h) time and O(h) space, n = nodes in the tree, h = height of the tree
        result = None
        def helper(node, path): # visit every node O(n) time
            nonlocal result
            if node:
                c = chr(node.val + ord('a'))
                path.append(c)
                if not node.left and not node.right:
                    s = "".join(path[::-1]) # needs to be constructed O(h) times (max number of leaves)
                    if result is None or result > s:
                        result = s
                helper(node.left, path)
                helper(node.right, path)
                path.pop()
            return result
        return helper(root, [])