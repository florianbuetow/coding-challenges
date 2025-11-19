# O(n) time and space
# link: https://leetcode.com/problems/sort-vowels-in-a-string/

from collections import defaultdict
class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vovels = 'AEIOUaeiou'
        counter = defaultdict(int)
        for c in s:
            if c in vovels:
                counter[c] += 1
        for i in range(len(s)):
            c = s[i]
            if c in vovels:
                for v in vovels:
                    if counter[v] > 0:
                        s[i] = v
                        counter[v] -= 1
                        break
        return "".join(s)
