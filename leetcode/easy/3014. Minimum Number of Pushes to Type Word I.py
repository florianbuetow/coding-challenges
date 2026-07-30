# link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/


class Solution:
    def minimumPushes(self, word: str) -> int:
        # O(n log n) time and O(n) space
        count = [0] * 26
        for c in word:
            i = ord(c) - ord('a')
            count[i] += 1

        keys = [1] * 8
        key_index = 0

        total_key_pushes = 0
        count.sort()
        while count and count[-1] > 0:
            pushes = count.pop()
            total_key_pushes += keys[key_index] * pushes
            keys[key_index] += 1
            key_index += 1
            key_index %= len(keys)
        return total_key_pushes
