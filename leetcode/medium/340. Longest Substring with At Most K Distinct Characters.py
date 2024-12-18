class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # O(n) time and O(k) space, n = len(s), k = number of distinct characters
        # link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
        result = left = 0
        counters = {}
        for right, c in enumerate(s):
            counters[c] = counters.get(c, 0) + 1
            while len(counters) > k and left <= right:
                c = s[left]
                counters[c] -=1
                if counters[c] == 0:
                    del counters[c]
                left += 1
            result = max(result, (right + 1) - left)
        return result
