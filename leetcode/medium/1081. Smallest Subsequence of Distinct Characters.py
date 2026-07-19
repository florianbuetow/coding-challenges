# link: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

from collections import defaultdict


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # O(n) time and space
        result = []
        freq = defaultdict(int)
        for i, c in enumerate(s):
            freq[c] += 1

        added = set()
        for c in s:
            freq[c] -= 1
            if c not in added:
                while result and result[-1] > c and freq[result[-1]]:
                    added.remove(result.pop())
                added.add(c)
                result.append(c)
        return "".join(result)
