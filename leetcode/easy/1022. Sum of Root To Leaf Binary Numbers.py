# link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # O(n) time and O(1) space
        result = 0

        def helper(node, val):
            nonlocal result
            val += node.val
            if node.left or node.right:
                val *= 2
                if node.left:
                    helper(node.left, val)
                if node.right:
                    helper(node.right, val)
            else:
                result += val

        helper(root, 0)
        return result
