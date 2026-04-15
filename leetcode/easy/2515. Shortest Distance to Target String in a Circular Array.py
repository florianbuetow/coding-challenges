# link: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/


from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # O(n) time and O(1) space
        def normalise(index):
            return (index + len(words)) % len(words)

        left = right = startIndex
        for distance in range(len(words)):
            if words[normalise(left)] == target: return distance
            if words[normalise(right)] == target: return distance
            left -= 1
            right += 1
        return -1
