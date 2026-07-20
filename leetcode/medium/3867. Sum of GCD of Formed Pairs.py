# link: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        # O(n log n) time and O(n) space
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        n_max = 0
        prefixGcd = []
        for n_cur in nums:
            n_max = max(n_max, n_cur)
            prefixGcd.append(math.gcd(n_cur, n_max))

        prefixGcd.sort()

        result = 0
        left, right = 0, len(prefixGcd) - 1
        while left < right:
            result += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        return result
