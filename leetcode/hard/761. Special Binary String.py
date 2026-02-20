# O(n*n) time and space
# link: https://leetcode.com/problems/special-binary-string/


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        result = []
        left = balance = 0
        for right in range(len(s)):
            balance += [-1, 1][s[right] == '1']
            if balance == 0:
                subsequence = self.makeLargestSpecial(s[left + 1:right])
                result.append(f"1{subsequence}0")
                left = right + 1
        result.sort(reverse=True)
        return ''.join(result)
