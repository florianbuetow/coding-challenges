# link: https://leetcode.com/problems/longest-common-suffix-queries/

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # O((n+m)*l) time and O(n*l) space, n = number of words, m = number of queryes, l = max length of any word or query
        def buildReverseTrie(arr):
            root = {}
            for i, word in enumerate(arr):
                t = root
                length = len(word)
                if 'meta' not in t or t['meta'][0] > length:
                    t['meta'] = [length, i]
                for j in range(length-1,-1,-1):
                    c = word[j]
                    if c not in t: t[c] = {}
                    t = t[c]
                    if 'meta' not in t or t['meta'][0] > length:
                        t['meta'] = [length, i] # saves the length and index of the shortest word with that prefix here
            return root

        def findLongestCommonSuffix(root, word):
            t = root
            res = t['meta'][1]
            for i in range(len(word)-1,-1,-1):
                c = word[i]
                res = t['meta'][1]
                if c not in t:
                    break
                t = t[c]
            res = t['meta'][1]
            return res


        trie = buildReverseTrie(wordsContainer)
        result = []
        for query in wordsQuery:
            res = findLongestCommonSuffix(trie, query)
            result.append(res)
        return result
