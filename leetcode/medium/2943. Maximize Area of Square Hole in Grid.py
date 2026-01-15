# O(n log n) time and O(1) space
# link: https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        if not hBars: return 1
        if not vBars: return 1
        if len(hBars) == 1: return 4
        if len(vBars) == 1: return 4

        cur_height = max_height = 1
        for cur_row, nxt_row in pairwise(hBars):
            if cur_row + 1 != nxt_row:
                cur_height = 0
            cur_height += 1
            max_height = max(cur_height, max_height)

        cur_width = max_width = 1
        for cur_col, nxt_col in pairwise(vBars):
            if cur_col + 1 != nxt_col:
                cur_width = 0
            cur_width += 1
            max_width = max(cur_width, max_width)

        result = min(max_height, max_width) + 1
        result *= result
        return result
