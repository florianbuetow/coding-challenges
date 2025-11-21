# O(n*n) time and O(n) space
# link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        prefix = {}
        postfix = {}
        for i in range(len(s)):
            c = s[i]
            if c not in prefix:
                prefix[c] = i
            postfix[c] = i

        result = set()
        for a in prefix:
            for i in range(prefix[a] + 1, postfix[a]):
                palindrome = f"{a}{s[i]}{a}"
                result.add(palindrome)
        return len(result)
