# O(n*n) time and O(1) space
# link: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        result = 0
        points.sort(key=lambda point: -point[1])
        points.sort(key=lambda point: point[0])

        for idx in range(len(points) - 1):
            min_y, max_y = float('-inf'), points[idx][1]
            for jdx in range(idx + 1, len(points)):
                y = points[jdx][1]
                if y > min_y and y <= max_y:
                    result += 1
                    min_y = y
                if y == max_y:
                    break
        return result
