# O(n) time and O(1) space
# link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([[-1, +1][op[1] == '+'] for op in operations])
