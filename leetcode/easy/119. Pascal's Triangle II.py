# link: https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # O(n) time and O(1) space
        def getVal(arr, idx):
            if idx < 0 or idx >= len(arr):
                return 0
            return arr[idx]

        curr = [1]
        for _ in range(rowIndex):
            next = []
            for i in range(len(curr)+1):
                val = 0
                val += getVal(curr, i-1)
                val += getVal(curr, i+0)
                next.append(val)
            curr = next
        return curr
