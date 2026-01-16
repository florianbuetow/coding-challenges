# O((n+m)log(n+m)) time and O(n + m) space
# link: https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def distances(fences):
            res = set()
            fences.sort()
            for x, y in combinations(fences, 2):
                res.add(y - x)
            return res

        result = distances([1, n] + vFences)
        result &= distances([1, m] + hFences)
        if not result:
            result = -1
        else:
            result = (max(result) ** 2) % (10 ** 9 + 7)
        return result
