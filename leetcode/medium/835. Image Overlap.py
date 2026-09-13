# link: https://leetcode.com/problems/image-overlap/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # O(n^4) time and O(1) space

        n = len(img1)
        def overlap(dx, dy):
            res = 0
            for y1 in range(n):
                y2 = y1 + dy
                if 0 > y2 or y2 >= n: continue
                for x1 in range(n):
                    x2 = x1 + dx
                    if 0 > x2 or x2 >= n: continue
                    if img1[y1][x1] + img2[y2][x2] == 2:
                        res += 1
            return res

        result = 0
        for dy in range(-n, n):
            for dx in range(-n, n):
                result = max(result, overlap(dx, dy))
        return result
