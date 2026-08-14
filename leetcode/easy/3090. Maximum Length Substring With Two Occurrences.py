# link: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # O(n) time and O(1) space
        result = left = 0
        window = defaultdict(int)
        for right, c in enumerate(s):
            window[c] += 1
            while window[c] > 2:
                window[s[left]] -= 1
                left += 1
            window_size = right - left + 1
            result = max(result, window_size)
        return result
