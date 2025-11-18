class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/1-bit-and-2-bit-characters
        bits.reverse()
        result = False
        while bits:
            bit = bits.pop()
            if bit == 0:
                result = True
            else:
                result = False
                bits.pop()
        return result
