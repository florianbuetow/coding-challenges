# link: https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # O(n log n) time and O(n) space
        def sumDigits(s):
            return str(sum([int(c) for c in s])) if s else ''

        while len(s) > k:
            groups = []
            index = 0
            while index < len(s):
                groups.append('')
                while index < len(s) and len(groups[-1]) != k:
                    groups[-1] += s[index]
                    index+=1
            s = ''.join(sumDigits(grp) for grp in groups)
        return s
