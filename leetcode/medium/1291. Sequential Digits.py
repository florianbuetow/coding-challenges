# link: https://leetcode.com/problems/sequential-digits/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # O(1) time and space
        result = []
        s = '123456789'
        for size in range(len(str(low)),  len(str(high))+1):
            for i in range(len(s)-size+1):
                n = int(s[i:i+size])
                if n >= low and n <= high:
                    result.append(n)
        return result
