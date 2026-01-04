# O(n*sqrt(m)) time and O(1) space
# link: https://leetcode.com/problems/four-divisors

class Solution(object):
    def sumFourDivisors(self, nums):
        result = 0
        for n in nums:
            divisors = []
            for d in range(1, int(n**0.5) + 1):
                if n % d == 0:
                    divisors.append(d)
                    if d != n // d: divisors.append(n // d)
                    if len(divisors) > 4: break
            if len(divisors) == 4:
                result += sum(divisors)
        return result
