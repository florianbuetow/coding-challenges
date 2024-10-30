from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # O(n log n) time and O(n) space
        # link: https://leetcode.com/problems/robot-collisions/
        data = []
        for index in range(len(positions)):
            data.append([positions[index], healths[index], directions[index], index])
        data.sort()

        stack, result = [], []
        index = -1
        for _, h, d, j in data:
            index += 1
            if d == 'L' and (not stack or data[stack[-1]][2] == 'L'):
                result.append([j, h])
                continue
            if d == 'R' or not stack:
                stack.append(index)
                continue
            insert = True
            while stack and data[stack[-1]][2] == 'R':
                prev_index = stack.pop() # delete robot from stack
                prev_h = data[prev_index][1]
                curr_h = data[index][1]
                if curr_h > prev_h:
                    # reduce health of survivor
                    data[index][1] -= 1
                    continue
                elif curr_h < prev_h:
                    # put robot back on stack and reduce health
                    stack.append(prev_index)
                    data[prev_index][1] -= 1
                    insert = False
                    break
                else:
                    # annihilation
                    insert = False
                    break
            if insert:
                stack.append(index)

        for index in stack:
            result.append([data[index][3], data[index][1]])

        result.sort()
        result = [h for _, h in result]

        return result