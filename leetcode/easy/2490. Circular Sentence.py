class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/circular-sentence
        prev, flag = sentence[-1], True
        for curr in sentence:
            if flag and prev != curr:
                return False
            if curr == ' ':
                flag = True
            else:
                flag = False
                prev = curr
        return True
