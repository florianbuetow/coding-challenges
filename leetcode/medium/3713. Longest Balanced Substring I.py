# O(n*n) time and O(n) space
# link: https://leetcode.com/problems/longest-balanced-substring-i/

class Solution:
    def longestBalanced(self, s: str) -> int:
        result = 1
        for left in range(len(s)):
            histogram = [0] * 26
            chars, max_frequency, result_max = 0, 0, 0
            for right in range(left, len(s)):
                histogram[ord(s[right]) % 26] += 1
                cur_frequency = histogram[ord(s[right]) % 26]
                if cur_frequency == 1:
                    chars += 1
                if cur_frequency > max_frequency:
                    max_frequency = cur_frequency
                    result_max = 1
                elif cur_frequency == max_frequency:
                    result_max += 1
                if result_max == chars:
                    result = max(result, right - left + 1)
        return result
