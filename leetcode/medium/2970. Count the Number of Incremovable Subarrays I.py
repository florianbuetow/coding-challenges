class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        # O(n*n) time and space
        n = len(nums)
        memory = {}
        def isSorted(left, right):
            if left >= right:
                return True
            key = (left, right)
            if key not in memory:
                memory[key] = (nums[right-1] < nums[right]) and isSorted(left, right - 1)
            return memory[key]

        def canRemoveSubarrayBetween(left, right):
            if left > right:
                return False
            if not isSorted(0, left-1):
                return False
            if not isSorted(right+1, n-1):
                return False
            if left < 1 or right > n - 2:
                return True
            return nums[left-1] < nums[right+1]

        result = 0
        for left in range(n):
            for right in range(left, n):
                if canRemoveSubarrayBetween(left, right):
                    result += 1
        return result