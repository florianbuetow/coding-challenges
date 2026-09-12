# link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # O(n) time and O(h) space, n = nodes, h = tree height
        result = 0
        def helper(node):
            nonlocal result
            total_sum = total_cnt = 0
            if node:
                left_sum, left_cnt = helper(node.left)
                right_sum, right_cnt = helper(node.right)
                total_sum = left_sum + right_sum + node.val
                total_cnt = left_cnt + right_cnt + 1
                if node.val == total_sum // total_cnt:
                    result += 1
            return total_sum, total_cnt
        helper(root)
        return result
