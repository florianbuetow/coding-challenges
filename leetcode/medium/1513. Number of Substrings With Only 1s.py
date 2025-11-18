# O(n) time and O(1) space
# link: https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:
        result = left = right = 0
        while right < len(s):
            left = right
            while left < len(s) and s[left] != '1': # find the next 1
                left += 1
            right = left
            while right < len(s) and s[right] != '0': # find the next 0
                right += 1
            for n in range(1, right - left + 1):
                result += n
            result %= 10**9+7
        return result
