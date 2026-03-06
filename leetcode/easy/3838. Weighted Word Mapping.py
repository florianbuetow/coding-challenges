# link: https://leetcode.com/problems/weighted-word-mapping/

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # O(n*k) time and O(n) space, n words, k avg word length
        def calcWeight(word):
            weight = 0
            for c in word:
                weight += weights[ord(c) - ord('a')]
            return weight

        result = []
        for word in words:
            print(word, calcWeight(word), calcWeight(word)%26)
            result.append(chr(ord('z') - (calcWeight(word) % 26)))
        return ''.join(result)
