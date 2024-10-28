from collections import defaultdict
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/count-substrings-without-repeating-character/
        result = left = 0
        window = defaultdict(int)
        for right in range(len(s)):
            window[s[right]] += 1
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            result += (right - left) + 1
        return result

