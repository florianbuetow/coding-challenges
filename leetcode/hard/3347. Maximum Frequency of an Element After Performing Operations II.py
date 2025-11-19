# O(n log n) time and O(n) space
# link: https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        result = 0
        nums.sort()
        freq = Counter(nums)
        num_target = set()
        for n in nums:
            num_target.add(n+k)
            num_target.add(n)
            num_target.add(n-k)
        num_target = list(num_target)
        num_target.sort()

        for n in num_target:
            min_n = n - k
            max_n = n + k
            start_index = bisect.bisect_left(nums, min_n)
            end_index = bisect.bisect_right(nums, max_n)
            window_size = end_index - start_index
            if window_size > 0:
                maxOperations = window_size - freq.get(n, 0)
                maxFrequency = min(maxOperations, numOperations) + freq.get(n, 0)
                result = max(result, maxFrequency)
        return result
