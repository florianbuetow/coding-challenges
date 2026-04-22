# link: https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # O(m*l + n*l) time and O(m*l) space, n = len(queries), m = len(dictionary), l = max length of words in dictionary
        def buildTrie(words):
            root = {}
            for word in words:
                t = root
                for c in word:
                    if c not in t:
                        t[c] = {}
                    t = t[c]
                t['marker'] = True
            return root

        def helper(node, word, index, edits):
            if edits < 0:  return False
            if len(word) == index: return 'marker' in node
            c = word[index]
            if c in node:
                if helper(node[c], word, index+1, edits): return True
            return any(helper(node[c], word, index+1, edits-1) for c in node)

        def isMatch(trie, word):
            return helper(trie, word, 0, 2)

        trie = buildTrie(dictionary)

        result = []
        for word in queries:
            if isMatch(trie, word):
                result.append(word)
        return result
