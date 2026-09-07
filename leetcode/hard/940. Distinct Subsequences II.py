# link: https://leetcode.com/problems/distinct-subsequences-ii/

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # O(n) time and O(1) space
        result = 0
        memory = [0] * 26
        for c in s:
            idx = ord(c) % 26
            delta = result + 1 - memory[idx]
            memory[idx] = (memory[idx] + delta) % 1000000007
            result += delta
            result %= 1000000007
        return result
