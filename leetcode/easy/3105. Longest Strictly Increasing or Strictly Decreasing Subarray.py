class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        def longestSubarray(arr, isMonotonic):
            max_length = length = 1
            for i in range(1, len(nums)):
                if isMonotonic(arr[i-1], arr[i]):
                    length += 1
                else:
                    length = 1
                max_length = max(max_length, length)
            return max_length

        return max(longestSubarray(nums, lambda a, b: a < b), longestSubarray(nums, lambda a, b: a > b))