# link: https://leetcode.com/problems/count-binary-substrings/


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # O(n) time and O(1) space
        result = prev = 0
        count = [0, 0]
        for curr in s:
            curr = int(curr)
            if prev != curr:
                count[curr] = 0
                prev = curr
            count[curr] += 1
            if count[curr] <= count[1 - curr]:
                result += 1
        return result
