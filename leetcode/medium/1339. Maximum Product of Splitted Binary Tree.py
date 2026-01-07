# O(n) time and space
# link: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []
        def helper(node):
            if not node:
                return 0
            sum_left = helper(node.left)
            sum_right = helper(node.right)
            sum_node = node.val + sum_left + sum_right
            subtree_sums.append(sum_node)
            return sum_node
        helper(root)
        result = -float('inf')
        for n in subtree_sums:
            f1 = subtree_sums[-1] - n
            f2 = n
            result = max(result, f1 * f2)
        return result % (10 ** 9 + 7)
