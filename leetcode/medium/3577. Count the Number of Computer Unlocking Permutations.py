# O(n) time and O(1) space
# link: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
        result = 1
        for i in range(2, len(complexity)):
            result *= i
            result %= 10**9+7
        return result
