from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # O(n) time and space
        # link: https://leetcode.com/problems/even-odd-tree/
        q = deque([[root, True]])        
        while q: 
            prev_node = None
            for _ in range(len(q)):
                node, even = q.popleft()                
                if node.val % 2 == [1, 0][even]: return False
                if prev_node and [prev_node.val <= node.val, prev_node.val >= node.val][even]:
                    return False
                prev_node = node
                if node.left: q.append([node.left, not even])
                if node.right: q.append([node.right, not even])                
        return True