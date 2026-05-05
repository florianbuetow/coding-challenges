# link: https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(n) time and O(1) space
        def get_length(node: Optional[ListNode]) -> int:
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = get_length(head)
        if length in [0, 1]: return head
        k = k % length
        if k <= 0: return head

        new_head = None
        prev, curr = None, head
        for _ in range(length - k):
            prev = curr
            curr = curr.next
        prev.next = None

        new_head = curr
        while curr.next:
            curr = curr.next
        curr.next = head

        return new_head
