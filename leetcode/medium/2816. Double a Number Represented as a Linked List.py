from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time and O(n) stack space
        # link: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
        def helper(node):
            if not node:
                return 0
            value = 2 * node.val + helper(node.next)
            carry = value // 10
            node.val = value % 10
            return carry

        carry = helper(head)
        if carry: head = ListNode(carry, head)
        return head
