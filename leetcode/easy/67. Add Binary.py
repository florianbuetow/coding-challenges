# O(n) time and space
# link: https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        c = []
        carry = 0
        while carry or a or b:
            digit = carry
            if a:
                digit += int(a.pop())
            if b:
                digit += int(b.pop())
            carry = digit // 2
            digit = digit % 2
            c.append(f"{digit}")
        return "".join(c[::-1])
