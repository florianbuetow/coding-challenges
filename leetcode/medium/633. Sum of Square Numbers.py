class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # O(log sqrt(c)) time and O(1) space
        low, high = 0, floor(c ** 0.5)
        while low <= high:
            summ = low ** 2 + high ** 2
            if summ < c:
                low += 1
            elif summ > c:
                high -= 1
            elif summ == c:
                return True
        return False
