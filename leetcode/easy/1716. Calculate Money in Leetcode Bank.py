# O(n) time and O(1) space
# link: https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0
        monday = 0
        yesterday = 0
        for i in range(n):
            if i % 7 == 0:
                monday += 1
                result += monday
                yesterday = monday
            else:
                yesterday += 1
                result += yesterday
        return result
