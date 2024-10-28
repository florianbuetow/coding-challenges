from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left = None
#         self.right = right = None

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # O(n) time and space, n = number of nodes in the tree
        # link: https://leetcode.com/problems/cousins-in-binary-tree-ii/

        def helper(values: List, parents: List[Optional[TreeNode]]) -> List:
            total_sum = sum(values)
            new_values = []
            for i in range(len(values)):
                new_value = total_sum
                for j in range(max(i - 1, 0), min(i + 2, len(values))):
                    if parents[i] == parents[j]:
                        # i and j are siblings, not cousins
                        new_value -= values[j]
                new_values.append(new_value)
            return new_values

        q = deque([(root, None)])  # BFS starting at the root
        while q:
            values, parents, nodes = [], [], []
            for _ in range(len(q)):
                node, parent = q.popleft()
                values.append(node.val)
                parents.append(parent)
                nodes.append(node)

            new_values = helper(values, parents)

            for node, value in zip(nodes, new_values):
                node.val = value
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

        return root
