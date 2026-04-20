# link: https://leetcode.com/problems/two-furthest-houses-with-different-colors/


from collections import defaultdict
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # O(n) time and O(n) space
        max_color_dist = 0
        min_color_pos = defaultdict(int)
        for curr_color_pos, curr_color in enumerate(colors):
            if curr_color not in min_color_pos:
                min_color_pos[curr_color] = curr_color_pos
            for other_color, other_color_pos in min_color_pos.items():
                if other_color != curr_color:
                    dist = curr_color_pos - other_color_pos
                    max_color_dist = max(dist, max_color_dist)
        return max_color_dist
