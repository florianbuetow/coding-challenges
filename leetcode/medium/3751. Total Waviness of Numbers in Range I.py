# link: https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # O(n) time and O(log n) space
        def inc(number):
            idx = 0
            carry = 1
            while carry:
                if idx == len(number):
                    number.append(0)
                number[idx] += carry
                carry = number[idx] // 10
                number[idx] %= 10
                idx += 1

        def getWeaviness(number):
            res = 0
            for idx in range(len(number)):
                if isWeavy(idx, number):
                    res +=1
            return res

        def isWeavy(idx, number):
            if idx <= 0 or idx >= len(number) - 1: return False
            if number[idx-1] < number[idx] > number[idx+1]: return True
            if number[idx-1] > number[idx] < number[idx+1]: return True
            return False

        result = 0
        curr = [int(digit) for digit in str(num1)][::-1]
        for _ in range(num2 - num1 + 1):
            result += getWeaviness(curr)
            inc(curr)
        return result
