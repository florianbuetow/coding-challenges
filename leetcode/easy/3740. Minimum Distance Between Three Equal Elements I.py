# O(n) time and space
# link: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        lookup = defaultdict(list)
        for i, n in enumerate(nums):
            lookup[n].append(i)

        result = float('inf')
        for n in lookup:
            if len(lookup[n]) >= 3:
                for pos in range(len(lookup[n])-2):
                    i = lookup[n][pos+0]
                    k = lookup[n][pos+1]
                    j = lookup[n][pos+2]
                    dist = abs(i-j) + abs(j-k) + abs(k-i)
                    result = min(result, dist)
        if result == float('inf'):
            result = -1
        return result
