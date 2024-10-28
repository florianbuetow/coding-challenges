# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head1: Optional[ListNode]) -> None:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/reorder-list/

        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        def reverse(node):
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev

        def getNthAndPrev(node, n):
            prev = None
            for _ in range(n):
                prev = node
                node = node.next
            return prev, node

        def zipLists(node1, node2):
            head = node1
            while node2:
                next1, next2 = node1.next, node2.next
                node1.next, node2.next = node2, next1
                node1, node2 = next1, next2
            return head

        n = getLength(head1)
        if n <= 2: return head1

        tail, head2 = getNthAndPrev(head1, n // 2)
        if n %2 == 1:
            head2 = head2.next
            tail = tail.next
        tail.next = None
        
        head2 = reverse(head2)
        return zipLists(head1, head2)

