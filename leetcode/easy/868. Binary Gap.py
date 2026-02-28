# link: https://leetcode.com/problems/binary-gap/


class Solution:
    def binaryGap(self, n: int) -> int:
        # O(n) time and O(1) space
        result = idx = 0
        pos = []
        while n:
            if n % 2:
                pos.append(idx)
                if len(pos) == 2:
                    result = max(result, abs(pos[0] - pos[1]))
                    pos = [pos[1]]
            idx += 1
            n //= 2
        return result
