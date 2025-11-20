# O(sqrt(c) * log c) time and O(1) space
# link: https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def findB(target):
            left, right = 0, target
            while left <= right:
                mid = (left + right) // 2
                val = mid * mid
                if val < target:
                    left = mid + 1
                elif val > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        a = 0
        while 2 * a*a <= c:
            b = findB(c - a*a)
            if b >= 0 and a**2 + b**2 == c:
                return True
            a += 1
        return False
