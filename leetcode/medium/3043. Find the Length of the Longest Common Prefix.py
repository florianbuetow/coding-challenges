# link: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # O(n) time and space
        if len(arr1) < len(arr2):
            return self.longestCommonPrefix(arr2, arr1)

        def buildTrie(arr):
            trie = {}
            for n in arr:
                t = trie
                for c in str(n):
                    if c not in t:
                        t[c] = {}
                    t = t[c]
            return trie

        result = 0
        trie = buildTrie(arr1)
        for n in arr2:
            t = trie
            length = 0
            for c in str(n):
                if c in t:
                    t = t[c]
                    length += 1
                else:
                    break
            result = max(result, length)
        return result
