# O(n log n) time and O(1) space
# link: https://leetcode.com/problems/construct-target-array-with-multiple-sums/

import heapq
from heapq import heappop, heappush
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sum_all = sum(target)
        for i in range(len(target)):
            target[i] = -target[i]
        heapq.heapify(target)
        while -target[0] != 1:
            max_val = -target[0]
            sum_rest = sum_all - max_val
            if sum_rest > 0:
                n = max((max_val - 1) // sum_rest, 1)
                sum_all -= n * sum_rest
                new_val = max_val - n * sum_rest
                if new_val < 1:
                    return False
                heappop(target)
                heappush(target, -new_val)
            else:
                return False
        return True
