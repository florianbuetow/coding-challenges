# link: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # O(n) time and O(1) space
        result, counter, sum_is_odd = 0, [1, 0], False
        for n in arr:
            if n % 2: sum_is_odd = not sum_is_odd
            result += counter[not sum_is_odd]
            counter[sum_is_odd]+=1
        result %= 10**9+7
        return result
