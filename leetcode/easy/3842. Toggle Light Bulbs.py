# link: https://leetcode.com/problems/toggle-light-bulbs/

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        # O(n) time and space
        bits = [0] * 100
        for idx in bulbs:
            idx -= 1
            bits[idx] = (bits[idx] + 1) % 2
        return [idx for idx, bit in enumerate(bits, start=1) if bit == 1]
