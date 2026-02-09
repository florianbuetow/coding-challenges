# O(n) time and space
# link: https://leetcode.com/problems/balance-a-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getValues(node, values):
            if node:
                getValues(node.left, values)
                values.append(node.val)
                getValues(node.right, values)
            return values

        def buildTree(l, r, values):
            node = None
            if l <= r:
                mid = (l + r) // 2
                node = TreeNode(values[mid])
                node.left = buildTree(l, mid - 1, values)
                node.right = buildTree(mid + 1, r, values)
            return node

        values = getValues(root, [])
        return buildTree(0, len(values) - 1, values)
