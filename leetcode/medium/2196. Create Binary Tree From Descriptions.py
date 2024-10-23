# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # O(n) time and space

        # construct the tree
        nodes, parents = {}, {}
        for p_id, c_id, isLeft in descriptions:
            child = nodes.get(c_id, TreeNode(c_id))
            parent = nodes.get(p_id, TreeNode(p_id))
            if isLeft:
                parent.left = child
            else:
                parent.right = child
            nodes[parent.val] = parent
            nodes[child.val] = child
            parents[child.val] = parent.val

        # find the node that doesn't have a parent
        for node_id in nodes:
            if node_id not in parents:
                return nodes[node_id]
