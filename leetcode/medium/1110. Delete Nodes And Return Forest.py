# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # O(n) time and space

        def helper(parent, node, target_values, result):
            if not node:
                return

            if node.val in target_values:
                # (current) node needs to be removed
                if parent:
                    # unlink node from parent
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                helper(None, node.left, target_values, result)
                helper(None, node.right, target_values, result)
            else:
                if not parent:
                    # node is the root of a subtree and needs to be added to the result
                    result.append(node)
                helper(node, node.left, target_values, result)
                helper(node, node.right, target_values, result)

        result = []
        helper(None, root, set(to_delete), result)
        return result
