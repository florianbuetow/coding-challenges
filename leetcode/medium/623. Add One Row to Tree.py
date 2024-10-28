# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # O(n) time and space
        # link: https://leetcode.com/problems/add-one-row-to-tree/
        if depth == 1:
            root = TreeNode(val, left=root, right=None)
        else:
            q = deque([root])
            while q:
                depth -=1
                for _ in range(len(q)):
                    node = q.popleft()
                    if depth == 1:
                        node.left = TreeNode(val, left=node.left, right=None)
                        node.right = TreeNode(val, left=None, right=node.right)
                    else:
                        if node.left: q.append(node.left)
                        if node.right: q.append(node.right)
        return root