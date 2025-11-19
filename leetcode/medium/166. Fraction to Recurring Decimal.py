# O(denominator * log denominator) time and O(denominator * log denominator) space
# link: https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'

        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
        numerator, denominator = abs(numerator), abs(denominator)

        intdiv, rest = numerator // denominator, numerator % denominator
        result.append(str(intdiv))
        numerator = rest

        if numerator != 0: result.append('.')
        seen = dict()
        while numerator != 0:
            if numerator in seen:
                pos = seen[numerator]
                result = result[:pos] + ['('] + result[pos:] + [')']
                break
            else:
                seen[numerator] = len(result)
            numerator *= 10
            intdiv, rest = numerator // denominator, numerator % denominator
            result.append(str(intdiv))
            numerator = rest

        return "".join(result)
