class Solution:
    def compressedString(self, word: str) -> str:
        # O(n) time and space
        # link: https://leetcode.com/problems/string-compression-iii
        compressed_word = []
        prev_c = None
        counter = 0
        for i in range(len(word)):
            c = word[i]
            if i > 0 and (counter == 9 or c != prev_c):
                compressed_word.append(str(counter) + prev_c)
                counter = 0
            prev_c = c
            counter += 1

        if counter:
            compressed_word.append(str(counter) + prev_c)
        return "".join(compressed_word)
