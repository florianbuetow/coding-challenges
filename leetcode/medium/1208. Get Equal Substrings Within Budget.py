class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # O(n) time and O(1) space
        result = left = cost = 0
        for right in range(len(s)):
            c1, c2 = s[right], t[right]
            if c1 != c2: cost += abs(ord(c1) - ord(c2))
            while cost > maxCost:
                c1, c2 = s[left], t[left]
                if c1 != c2: cost -= abs(ord(c1) - ord(c2))
                left += 1
            result = max(result, right - left + 1)
        return result