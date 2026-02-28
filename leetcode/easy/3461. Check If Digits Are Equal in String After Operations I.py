# link: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # O(n) time and O(1) space
        def helper(arr):
            for i in range(len(arr) - 1):
                arr[i] = (arr[i] + arr[i+1]) % 10
            arr.pop()

        arr = [int(digit) for digit in s]
        while len(arr) > 2:
            helper(arr)
        return arr[0] == arr[1]
