class Solution:
    def numSteps(self, s: str) -> int:
        # O(n) time and O(1) space, n = len(s)
        # link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
        steps = carry = 0
        for i in range(len(s)-1,-1,-1):
            digit = int(s[i])
            digit += carry
            if digit == 1 and i == 0:
                break
            carry = digit // 2
            if digit % 2 != 0:
                digit += 1
                carry = digit // 2
                steps += 1
            steps += 1
        return steps