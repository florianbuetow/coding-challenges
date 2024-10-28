from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # O(n*m) time and O(n+m) space, n = sum(len(words)), m = len(sentence)
        # link: https://leetcode.com/problems/replace-words/
        # idea: use a trie to find the shortest prefix match of a word
        trie = {}
        for word in dictionary:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['marker'] = True

        result = []
        prefix = []
        t = trie
        skip_to_space = False
        for c in sentence:
            if c == ' ':
                result.append("".join(prefix))
                skip_to_space = False
                prefix = []
                t = trie
            elif not skip_to_space:
                prefix.append(c)
                if t is not None and c in t:
                    t = t[c]
                    if 'marker' in t:
                        skip_to_space = True
                else:
                    t = None
        result.append("".join(prefix))
        return " ".join(result)