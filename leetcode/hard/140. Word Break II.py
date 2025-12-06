# O(2^n) time and O(2^n) space
# link: https://leetcode.com/problems/word-break-ii/


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = word

    def match_prefix(self, s: str, idx: int) -> int:
        matches = []
        node = self
        length = 0
        for i in range(idx, len(s)):
            c = s[i]
            if c not in node.children:
                break
            length += 1
            node = node.children[c]
            if node.is_word:
                matches.append(node.is_word)
        return matches


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # O(2^n) time and space, n = len(s), m = len(wordDict)
        root = TrieNode()
        for word in wordDict:
            root.insert(word)
        results = []

        @cache
        def prefix_helper(index: int) -> List[str]:
            return root.match_prefix(s, index)

        def helper(index: int, path: List[str]) -> None:
            if index >= len(s):
                results.append(" ".join(path))
            else:
                for prefix in prefix_helper(index):
                    path.append(prefix)
                    helper(index + len(prefix), path)
                    path.pop()

        helper(0, [])
        return results
