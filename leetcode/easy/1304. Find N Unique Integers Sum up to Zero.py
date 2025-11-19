# O(n) time and space
# link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0] if n % 2 == 1 else []
        for m in range(1, 1 + n//2):
            result.append(-m)
            result.append(m)
        return result
