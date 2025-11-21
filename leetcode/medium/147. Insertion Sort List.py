# O(n*n) time and O(n) space
# link: https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getLength(node):
            length = 0
            while node:
                node = node.next
                length += 1
            return length

        def insertionSort(prev, curr, depth):
            if depth > 0:
                curr.val = insertionSort(curr, curr.next, depth - 1)

            if prev:
                prev_val, curr_val  = prev.val, curr.val
                if prev_val > curr_val:
                    curr.val = prev_val
                    return curr_val
                return prev_val

        length = getLength(head)
        for depth in range(length):
            insertionSort(None, head, depth)
        return head
