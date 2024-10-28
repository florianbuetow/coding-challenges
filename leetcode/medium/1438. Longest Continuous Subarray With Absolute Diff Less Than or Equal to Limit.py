from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # O(n) time and space
        # link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
        # idea: use a monotonic stack to keep track of min and max element in window
        #       compute abs diff from these stacks
        max_stack, min_stack = deque(), deque()
        max_length = left = 0

        for right in range(len(nums)):
            while max_stack and max_stack[-1] < nums[right]:
                max_stack.pop()
            max_stack.append(nums[right])

            while min_stack and min_stack[-1] > nums[right]:
                min_stack.pop()
            min_stack.append(nums[right])

            while abs(max_stack[0] - min_stack[0]) > limit:
                if nums[left] == max_stack[0]: max_stack.popleft()
                if nums[left] == min_stack[0]: min_stack.popleft()
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length