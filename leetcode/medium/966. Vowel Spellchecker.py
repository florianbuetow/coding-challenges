# O(n*m) time and O(n) space, n = len(wordlist), m = len(queries)
# link: https://leetcode.com/problems/vowel-spellchecker/

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def maskVowels(word):
            vowels = 'aeiouAEIOU'
            res = []
            for c in word:
                if c in vowels:
                    res.append('.')
                else:
                    res.append(c)
            return "".join(res)

        words = set()
        words_lower = {}
        words_masked = {}
        for word in wordlist:
            words.add(word)
            word_lower = word.lower()
            word_masked = maskVowels(word_lower) # this is not explained well in the problem description, vovel errors + lowercase
            words_lower[word_lower] = words_lower.get(word_lower, word)
            words_masked[word_masked] = words_masked.get(word_masked, word)

        res = []
        for word in queries:
            word_lower = word.lower()
            word_masked = maskVowels(word_lower)

            if word in words:
                res.append(word)
            elif word_lower in words_lower:
                res.append(words_lower[word_lower])
            elif word_masked in words_masked:
                res.append(words_masked[word_masked])
            else:
                res.append("")
        return res
