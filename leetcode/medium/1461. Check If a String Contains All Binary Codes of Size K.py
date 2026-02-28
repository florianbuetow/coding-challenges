# link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # O(n*n) time and space
        codes = set()
        for i in range(len(s)-k+1):
            codes.add(s[i:i+k])
            if len(codes) == 2 ** k:
                return True
        return False
