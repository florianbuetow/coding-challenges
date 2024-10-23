class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # O(n) time and O(1) space
        # idea:     1. xor all numbers, the result is a bitmask with the value a xor b
        #           2. identify a bit that is different between a and b (for example the rightmost bit)
        #           3. xor all numbers that have that bit set
        #           4. the result will contain a, and b can be calculated using a xor bitmask

        bitmask = 0
        for n in nums:
            bitmask ^= n

        diffbit = bitmask & (-bitmask) # gets the rightmost 1-bit diff between a and b

        a = 0
        for n in nums:
            if n & diffbit: # xor all numbers that have the identified bit set
                a ^= n

        b = a ^ bitmask
        return [a, b]