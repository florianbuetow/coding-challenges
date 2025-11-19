# O(m log n) time and O(n) space, n = len(classes), m = n + extraStudents
# link: https://leetcode.com/problems/maximum-average-pass-ratio/

from heapq import heappop, heappush, heapify

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        result = 0

        def compute_factor(class_data):
            passing, total = class_data
            curr_ratio = passing / total
            next_ratio = (passing + 1) / (total + 1)
            return abs(curr_ratio - next_ratio)

        maxheap = [[-compute_factor(class_data), idx] for idx, class_data in enumerate(classes)]
        heapify(maxheap)

        for _ in range(extraStudents):
            idx = heappop(maxheap)[1]
            classes[idx][0] += 1
            classes[idx][1] += 1
            change_factor = compute_factor(classes[idx])
            heappush(maxheap, [-change_factor, idx])

        for passing, total in classes:
            result += passing / total
        return result / len(classes)
