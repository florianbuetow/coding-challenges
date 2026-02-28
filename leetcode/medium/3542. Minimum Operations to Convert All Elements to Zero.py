# link: https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        result = 0
        stack = []
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            if (not stack or stack[-1] < n) and n != 0:
                stack.append(n)
                result += 1
        return result
