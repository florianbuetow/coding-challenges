# O(n) time and space
# link: https://leetcode.com/problems/linked-list-frequency/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = defaultdict(int)
        while head:
            counter[head.val] += 1
            head = head.next
        head = prev = ListNode()
        for count in counter.values():
            prev.next = ListNode(count)
            prev = prev.next
        return head.next