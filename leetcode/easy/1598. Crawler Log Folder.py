class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # O(n) time and (1) space
        result = 0
        for op in logs:
            if op == './':
                continue
            elif op == '../':
                result = max(0, result - 1)
            else:
                result += 1
        return result