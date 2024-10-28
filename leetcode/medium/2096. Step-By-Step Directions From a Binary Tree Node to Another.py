# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # O(n) time and space
        # link: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
        def getPathToNode(node, target_value, path):
            if node:
                if node.val == target_value:
                    return True
                if node.left:
                    path.append([node.left.val, 'L'])
                    if getPathToNode(node.left, target_value, path): return True
                    path.pop()
                if node.right:
                    path.append([node.right.val, 'R'])
                    if getPathToNode(node.right, target_value, path): return True
                    path.pop()
            return False

        path_to_start = []
        if not getPathToNode(root, startValue, path_to_start): return ""
        path_to_start = path_to_start[::-1]

        path_to_dest = []
        if not getPathToNode(root, destValue, path_to_dest): return ""
        path_to_dest = path_to_dest[::-1]

        # find lowest common ancestor (lca)
        while path_to_start and path_to_dest and path_to_start[-1][0] == path_to_dest[-1][0]:
            path_to_start.pop()
            path_to_dest.pop()

        # walk up from start to lca
        result = ['U' * len(path_to_start)]

        # walk down from lca to dest
        while path_to_dest:
            result.append(path_to_dest.pop()[1])
        return "".join(result)