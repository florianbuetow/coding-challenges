# link: https://leetcode.com/problems/minimum-capacity-box/

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        # O(n) time and O(1) space
        result = -1
        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                if result < 0 or capacity[result] > capacity[i]:
                    result = i
        return result
