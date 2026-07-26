# O(n*n) time and space
# link: https://www.hackerrank.com/challenges/sherlock-and-anagrams

from collections import defaultdict

def sherlockAndAnagrams(s):
    n = len(s)
    signatures = defaultdict(int)

    for start in range(n):
        counts = [0] * 26
        for end in range(start, n):
            counts[ord(s[end]) - ord("a")] += 1
            signatures[tuple(counts)] += 1

    result = 0
    for count in signatures.values():
        result += count * (count - 1) // 2
    return result
