# O(n*m) time and O(n*m) space, n = len(words), m = length of longest word
# link: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def getSignature(w):
            histogram = [0] * 26
            for c in w:
                histogram[ord(c) % 26] += 1
            result = []
            for i in range(26):
                count = histogram[i]
                result.append(str(count)+',')
            return "".join(result)

        left, prev_signature = 0, ''
        for right in range(len(words)):
            curr = words[right]
            curr_signature = getSignature(curr)
            if prev_signature != curr_signature:
                words[left] = curr
                left += 1
            prev_signature = curr_signature

        while len(words) > left:
            words.pop()
        return words
