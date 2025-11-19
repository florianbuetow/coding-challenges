# O(n*m) time and O(1) space
# link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = prev = 0
        for row in bank:
            curr = sum(1 for c in row if c == '1')
            if curr == 0: continue
            result += prev * curr
            prev = curr
        return result
