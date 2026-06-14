# link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # O(n) time and O(1) space
        def reverse(node):
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev

        def split(node):
            head1 = node
            fast = slow = node
            prev = None
            while fast:
                prev = slow
                slow = slow.next
                fast = fast.next
                fast = fast.next
            head2 = slow
            prev.next = None
            return head1, head2

        lst1, lst2 = split(head)
        lst2 = reverse(lst2)

        result = 0
        while lst1 and lst2:
            result = max(result, lst1.val + lst2.val)
            lst1 = lst1.next
            lst2 = lst2.next
        return result
