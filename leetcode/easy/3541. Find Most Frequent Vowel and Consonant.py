# O(n) time and O(1) space
# link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        hist = [0] * 26
        for c in s:
            hist[ord(c)-ord('a')] += 1
        max_count = [0, 0]
        for i in range(26):
            c = chr(ord('a') + i)
            idx = [0, 1][c in 'aeiou']
            max_count[idx] = max(max_count[idx], hist[i])
        return sum(max_count)
