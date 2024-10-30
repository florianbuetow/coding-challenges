from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/trapping-rain-water/
        trapped_water = 0
        max_height = max_height_index = potentially_trapped_water = 0
        for index in range(len(height)):
            cur_height = height[index]
            if cur_height >= max_height:
                max_height = cur_height
                max_height_index = index
                trapped_water += potentially_trapped_water
                potentially_trapped_water = 0
            else:
                potentially_trapped_water += (max_height - cur_height)

        peak = max_height_index
        max_height = max_height_index = potentially_trapped_water = 0
        for index in range(len(height)-1, peak-1,-1):
            cur_height = height[index]
            if cur_height >= max_height:
                max_height = cur_height
                max_height_index = index
                trapped_water += potentially_trapped_water
                potentially_trapped_water = 0
            else:
                potentially_trapped_water += (max_height - cur_height)

        return trapped_water