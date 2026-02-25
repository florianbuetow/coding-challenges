# O(n*n) time and O(n) space
# link: https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        def getPredecessor(row, i):
            if i < 0 or i >= len(row):
                return 0
            return row[i]

        curr = [1]
        for _ in range(numRows):
            result.append(curr)
            next = []
            for i in range(len(curr)+1):
                val = 0
                val += getPredecessor(curr, i-1)
                val += getPredecessor(curr, i+0)
                next.append(val)
            curr = next
        return result
