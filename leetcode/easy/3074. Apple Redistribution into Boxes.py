# O(m + n log n) time and O(1) space, n boxes, m apples
# link: https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        apples = sum(apple)
        result = 0
        while apples > 0:
            apples -= capacity.pop()
            result += 1
        return result
