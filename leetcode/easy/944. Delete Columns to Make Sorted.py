# O(n*m) time and O(1) space
# link: https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        height, width = len(strs), len(strs[0])
        for x in range(width):
            prev_c = None
            for y in range(height):
                c = strs[y][x]
                if prev_c and c < prev_c:
                    result += 1
                    break
                prev_c = c
        return result
