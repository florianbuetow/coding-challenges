from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # O(1) time and space
        # link: https://leetcode.com/problems/open-the-lock/
        # idea: use BFS and terminate when we find target
        visited = set(deadends)
        q = deque([['0000', 0]])
        while q:
            lock_state, steps = q.popleft()
            if lock_state == target: return steps
            if lock_state in visited: continue
            visited.add(lock_state)
            for wheel in [0,1,2,3]:
                for delta in [-1, 1]:
                    next_state = []
                    for wheel_nr, digit in enumerate(lock_state):
                        if wheel_nr == wheel:
                            digit = (int(digit) + delta + 10) % 10
                        next_state.append(str(digit))
                    next_state = "".join(next_state)
                    q.append([next_state, steps + 1])
        return -1