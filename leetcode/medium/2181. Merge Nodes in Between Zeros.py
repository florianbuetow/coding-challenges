# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/merge-nodes-in-between-zeros/
        temp, summ = [], 0
        slow, prev, node = head, None, head
        while node:
            summ += node.val
            if node.val == 0:
                if summ != 0:
                    slow.val = summ
                    prev = slow
                    slow = slow.next
                summ = 0
            node = node.next

        if prev:
            prev.next = None
        return head