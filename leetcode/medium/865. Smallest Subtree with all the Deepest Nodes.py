# O(n) time and space
# link: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # O(n) time and space, n number of nodes
        parent = {}
        lvl, last_lvl = 0, []
        q = deque([[root, None]])

        # 1. Find deepest nodes
        while q:
            lvl += 1
            last_lvl.clear()
            for _ in range(len(q)):
                curr, prev = q.popleft()
                parent[curr] = prev
                if curr.left: q.append([curr.left, curr])
                if curr.right: q.append([curr.right, curr])
                last_lvl.append(curr)

        # 2. Find and return LCA of deepest nodes
        curr_lvl = last_lvl
        while len(curr_lvl) > 1:
            prev_lvl = set()
            while curr_lvl:
                prev_lvl.add(parent[curr_lvl.pop()])
            curr_lvl = list(prev_lvl)
        return curr_lvl.pop()




