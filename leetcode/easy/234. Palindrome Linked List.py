# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head1: Optional[ListNode]) -> bool:
        #O(n) time and O(1) space

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

        def getNthNodeAndPrev(node, n):
            prev = None
            for _ in range(n):
                prev = node
                node = node.next
            return prev, node

        n = getLength(head1)
        if n == 1:
            return True

        tail1, head2 = getNthNodeAndPrev(head1, n // 2)
        tail1.next = None

        if n % 2 == 1:
            head2 = head2.next
        head2 = reverse(head2)

        for _ in range(n//2):
            if head1.val != head2.val:
                return False
            head1, head2 = head1.next, head2.next

        return True
