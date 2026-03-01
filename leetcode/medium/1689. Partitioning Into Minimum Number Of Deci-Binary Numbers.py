# link: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        # O(log n) time and O(1) space
        result = 0
        for digit in n:
            digit = int(digit)
            result = max(result, digit)
            if result == 9:
                break
        return result
