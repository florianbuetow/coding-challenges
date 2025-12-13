# O(n * m + n log n) time and space n = len(codes), m = max length of any code
# link: https://leetcode.com/problems/coupon-code-validator/

class Solution:
    def validateCoupons(self, codes: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def isValidCode(code): # O(m) time
            if not code: return False
            for c in code.lower():
                if c.isalnum(): continue
                if c == '_': continue
                return False
            return True

        result = []
        for code, category, active in zip(codes, businessLine, isActive): # O(n) time
            if active and isValidCode(code):
                if category in ["electronics", "grocery", "pharmacy", "restaurant"]:
                    result.append([code, category])

        result.sort(key=lambda e: e[0]) # O(n log n)
        result.sort(key=lambda e: e[1]) # O(n log n)
        for i in range(len(result)):
            result[i] = result[i][0]
        return result
