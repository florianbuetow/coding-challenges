# O(n * m) time and O(m) space
# link: https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # O(n * m) time and O(m) space, n = num strings, m = string length
        n, m = len(strs), len(strs[0])
        memory = [1] * m
        for i in range(m):
            for j in range(i):
                keepRow = True
                for r in range(n):
                    if strs[r][j] > strs[r][i]:
                        keepRow = False
                        break
                if keepRow:
                    memory[i] = max(memory[i], memory[j] + 1)
        return m - max(memory)
