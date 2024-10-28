from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # O(n log n) time and O(1) space
        # link: https://leetcode.com/problems/bag-of-tokens
        tokens.sort(reverse=True)
        i = cur_score = max_score = 0
        while i < len(tokens):
            if tokens[-1] <= power:
                power -= tokens.pop()
                cur_score += 1
            else:
                if cur_score >= 1:
                    power += tokens[i] 
                    cur_score -= 1
                i += 1
            max_score = max(cur_score, max_score)
        return max_score