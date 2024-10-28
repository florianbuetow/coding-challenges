class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
        max_window = 0
        counters = {}
        left = 0
        for right, c in enumerate(s):
            counters[c] = counters.get(c, 0) + 1
            while len(counters) > 2:
                c = s[left]
                counters[c] -= 1
                if counters[c] == 0:
                    del counters[c]
                left += 1
            max_window = max(max_window, right - left + 1)
        return max_window