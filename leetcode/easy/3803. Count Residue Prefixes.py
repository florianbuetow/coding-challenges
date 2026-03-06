# link: https://leetcode.com/problems/count-residue-prefixes/

class Solution:
    def residuePrefixes(self, s: str) -> int:
        # O(n) time and space
        result = 0
        prefix_chars = set()
        for i in range(len(s)):
            prefix_chars.add(s[i])
            if len(prefix_chars) == (i+1) % 3:
                result += 1
        return result
