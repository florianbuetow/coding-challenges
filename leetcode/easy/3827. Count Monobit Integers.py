# link: https://leetcode.com/problems/count-monobit-integers/

class Solution:
    def countMonobit(self, n: int) -> int:
        # O(log n) time and O(1) space
        result = 1
        if n != 0:
            m = 1
            while m <= n:
                m = 2 * m + 1
                result +=1
        return result
