# link: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # O(n) time and O(1) space
        def hasZeros(n):
            return '0' in str(n)

        left, right = 0, n
        while hasZeros(left) or hasZeros(right):
            left += 1
            right -= 1
        return [left, right]
