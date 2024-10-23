class Solution:
    def tribonacci(self, n: int) -> int:
        # O(n) time and O(1) space
        window, index = [0, 1, 1], -1
        for index in range(n):
            window[index % 3] = sum(window)
        return window[(index+1) %3]