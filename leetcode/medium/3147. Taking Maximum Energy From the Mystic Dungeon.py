# O(n) time and O(1) space
# link: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        result = energy[-1]
        for i in range(len(energy)-1,len(energy)-k-1,-1):
            postfix_sum = 0
            for j in range(i, -1, -k):
                postfix_sum += energy[j]
                result = max(result, postfix_sum)
        return result
