# link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        # O(n) time and space
        counter = Counter(word)
        hist = [[count, c] for c, count in counter.items()]
        hist.sort(reverse=True)
        keypad = defaultdict(set)
        result = idx = 0
        for count, c in hist:
            pushes = len(keypad[idx]) + 1
            result += pushes * count
            keypad[idx].add(c)
            idx = (idx + 1) % 8
        return result
