# O(n) time and space
# link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums) # without this we would have O(n*n) time and O(1) space
        prev, curr = None, head
        while curr:
            next = curr.next
            if curr.val in nums:
                if not prev:
                    head = next
                else:
                    prev.next = next
            else:
                prev = curr
            curr = next
        return head
