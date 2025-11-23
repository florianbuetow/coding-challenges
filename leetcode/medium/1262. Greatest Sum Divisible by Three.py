# O(n) time and O(1) space
# link: https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        def findMinTwoWithRest(rest):
            mins = []
            for n in nums:
                if n % 3 == rest:
                    mins.append(n)
                    mins.sort()
                    if len(mins) > 2:
                        mins.pop()
            return mins

        total = sum(nums)
        minWithRest = [
            [0],
            findMinTwoWithRest(1),
            findMinTwoWithRest(2)
        ]
        result = 0
        for arr in minWithRest:
            tmp = 0
            for n in arr:
                tmp += n
                candidate = total - tmp
                if candidate % 3 == 0:
                    result = max(result, candidate)
        return result
