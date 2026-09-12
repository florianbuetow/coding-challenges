# link: https://leetcode.com/problems/unique-3-digit-even-numbers/

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # O(n) time and space
        counts = [0] * 10
        for digit in digits:
            counts[digit] += 1
        result = 0
        for d1 in range(1, 10):
            if counts[d1] == 0:
                continue
            counts[d1] -= 1
            for d2 in range(10):
                if counts[d2] == 0:
                    continue
                counts[d2] -= 1
                for d3 in range(0, 10, 2):
                    if counts[d3] > 0:
                        result += 1
                counts[d2] += 1
            counts[d1] += 1
        return result
