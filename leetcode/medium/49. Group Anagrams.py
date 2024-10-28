from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n*m) time and space, n:=number of words, m:= average word length
        # link: https://leetcode.com/problems/group-anagrams/
        def embed(word):
            vector = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                vector[index] += 1
            return tuple(vector)

        groups = defaultdict(list)
        for word in strs:
            v = embed(word)
            groups[v].append(word)

        result = [group for group in groups.values()]
        return result
