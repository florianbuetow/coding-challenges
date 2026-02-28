# link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits


from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # O(n) time and O(1) space
        def countBits(n):
            count = 0
            while n:
                count += n%2
                n //= 2
            return count

        buckets = defaultdict(list)
        for n in arr:
            count = countBits(n)
            buckets[count].append(n)

        for count in buckets:
            buckets[count].sort(reverse=True)

        result = []
        for count in range(max(buckets.keys())+1):
            while buckets[count]:
                result.append(buckets[count].pop())
        return result
