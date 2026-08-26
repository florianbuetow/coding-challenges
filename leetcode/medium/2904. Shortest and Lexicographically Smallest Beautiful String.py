# link: https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # O(n*k) time and O(n) space
        result = None
        left = right = ones = 0
        while right < len(s):
            c = s[right]
            if c == '1': ones += 1
            while ones > k or (ones == k and s[left] != '1'):
                c = s[left]
                if c == '1': ones -= 1
                left += 1
            right += 1
            if ones == k:
                word = s[left:right]
                if result is None:
                    result = word
                elif len(result) > len(word):
                    result = word
                elif len(result) == len(word) and word < result:
                    result = word

        return result if result else ""
