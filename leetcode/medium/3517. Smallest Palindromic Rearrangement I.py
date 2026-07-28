# link: https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # O(n) time and space
        hist = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            hist[idx] += 1
        prefix = []
        infix = []
        postfix = []
        for idx, count in enumerate(hist):
            while count > 0:
                char = chr(idx + ord('a'))
                if count % 2 == 1:
                    infix.append(char)
                    count -= 1
                else:
                    prefix.append(char)
                    postfix.append(char)
                    count -= 2
        postfix.reverse()
        return ''.join(prefix + infix + postfix)
