# O(m*n*k) time and O(m*n) space, k = len(strs)
# link: https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memory = []
        for _ in range(m + 1):
            memory.append([0] * (n+1))

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros-1,-1):
                for j in range(n, ones-1,-1):
                    memory[i][j] = max(
                        memory[i][j],
                        memory[i-zeros][j-ones] + 1
                    )
        return memory[m][n]
