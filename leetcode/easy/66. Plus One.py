# O(n) time and space
# link: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        while digits:
            digit = digits.pop() + carry
            result.append(digit % 10)
            carry = digit // 10
        if carry:
            result.append(carry)
        result.reverse()
        return result
