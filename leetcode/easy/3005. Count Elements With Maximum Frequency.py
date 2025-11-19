# O(n) time and O(m) space, n = len(nums), m = len(set(nums))
# link: https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        max_freq = 0
        for n in freq:
            max_freq = max(max_freq, freq[n])

        max_count = 0
        for n in freq:
            if freq[n] == max_freq:
                max_count += 1

        return max_freq * max_count
