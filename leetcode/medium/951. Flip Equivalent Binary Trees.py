# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # O(n) time and space, n = number of nodes in both trees
        # link: https://leetcode.com/problems/flip-equivalent-binary-trees/

        # If root1 is None, they are equivalent if root2 is also None
        if not root1:
            return not root2

        # Initialize queue to perform a breadth-first traversal, comparing nodes in pairs
        q = deque()
        q.append([root1, root2])

        while q:
            n1, n2 = q.popleft()

            # If one node is None and the other is not, trees are not equivalent
            if not n1 or not n2:
                if n1 or n2:
                    return False

            # If the values of the nodes do not match, trees are not equivalent
            if n1.val != n2.val:
                return False

            # Case: Both nodes have left and right children
            if n1.left and n1.right:
                # If n2 does not have both left and right children, they cannot be equivalent
                if not n2.left or not n2.right:
                    return False

                # Check if left subtrees match or need flipping
                if n1.left.val == n2.left.val:
                    q.append([n1.left, n2.left])  # No flip needed on the left
                elif n1.left.val == n2.right.val:
                    q.append([n1.left, n2.right])  # Flip left subtree
                else:
                    return False

                # Check if right subtrees match or need flipping
                if n1.right.val == n2.right.val:
                    q.append([n1.right, n2.right])  # No flip needed on the right
                elif n1.right.val == n2.left.val:
                    q.append([n1.right, n2.left])  # Flip right subtree
                else:
                    return False

            # Case: n1 has only a left child
            elif n1.left and not n1.right:
                if n2.left and n2.right:
                    return False  # n2 has both children, n1 does not

                # Check if the single child in n1 matches a single child in n2
                if n2.left:
                    q.append([n1.left, n2.left])
                elif n2.right:
                    q.append([n1.left, n2.right])
                else:
                    return False

            # Case: n1 has only a right child
            elif n1.right and not n1.left:
                if n2.left and n2.right:
                    return False  # n2 has both children, n1 does not

                # Check if the single child in n1 matches a single child in n2
                if n2.left:
                    q.append([n1.right, n2.left])
                elif n2.right:
                    q.append([n1.right, n2.right])
                else:
                    return False

            # Case: n1 has no children
            else:
                if n2.left or n2.right:
                    return False  # n2 has children, n1 does not

        # If all nodes match according to the rules above, trees are flip equivalent
        return True
