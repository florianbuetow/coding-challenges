# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
        result = [float('inf'), -1]
        position = 0
        prev, node = None, head
        firstCriticalPoint = lastCriticalPoint = None
        while node:
            position += 1
            if prev and node.next:
                if node.val > max(prev.val, node.next.val) or node.val < min(prev.val, node.next.val):
                    if firstCriticalPoint is None:
                        firstCriticalPoint = lastCriticalPoint = position
                    else:
                        result[0] = min(result[0], position - lastCriticalPoint)
                        lastCriticalPoint = position
                        result[1] = max(result[1], lastCriticalPoint - firstCriticalPoint)
            prev = node
            node = node.next
        if result[0] == float('inf'):
            result[0] = -1
        return result