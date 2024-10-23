# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # O(n) time and O(m) space, n = number of nodes in the tree, m = height of the tree

        def getPathToNode(curr_node, target_value, path):
            if curr_node:
                path.append(curr_node.val)
                if curr_node.val == target_value: return True
                if getPathToNode(curr_node.left, target_value, path): return True
                if getPathToNode(curr_node.right, target_value, path): return True
                path.pop()
            return False

        # Find the path from the root to p
        path_to_p = []
        getPathToNode(root, p, path_to_p)
        path_to_p = path_to_p[::-1]

        # Find the path from the root to q
        path_to_q = []
        getPathToNode(root, q, path_to_q)
        path_to_q = path_to_q[::-1]

        # Remove nodes from paths until paths diverge
        while path_to_q and path_to_p and path_to_q[-1] == path_to_p[-1]:
            path_to_p.pop()
            path_to_q.pop()

        return len(path_to_p) + len(path_to_q)