class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # O(n) time and space, n = len(words)
        def getHistogram(word):
            hist = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                hist[index] += 1
            return hist

        histogramms = []
        for word in words:
            histogramms.append(getHistogram(word))

        result = []
        for index in range(26):
            char = chr(ord('a') + index)
            occurence = float('inf')
            for hist in histogramms:
                occurence = min(hist[index], occurence)
            result.extend([char] * occurence)
        return result