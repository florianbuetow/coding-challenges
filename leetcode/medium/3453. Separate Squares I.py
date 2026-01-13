# O(n log n) time and O(1) space
# link: https://leetcode.com/problems/separate-squares-i/

class Solution:
    def separateSquares(self, squares):
        def calcAboveVsBelow(line):
            above = below = 0.0
            for _, y, l in squares:
                area = l * l
                if line <= y:
                    above += area
                elif line >= y + l:
                    below += area
                else:
                    below_area = area * ((line - y) / l)
                    above += area - below_area
                    below += below_area
            return above - below

        top, btm = -float('inf'), float('inf')
        for _, y, l in squares:
            top = max(top, y + l)
            btm = min(btm, y)

        for _ in range(70):
            line = (top + btm) / 2.0
            diff = calcAboveVsBelow(line)
            if diff <= 0:
                top = line
            else:
                btm = line
        return top
