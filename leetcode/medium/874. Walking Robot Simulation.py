# link: https://leetcode.com/problems/walking-robot-simulation/description

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # O(n) time and O(1) space
        tmp, obstacles = obstacles, defaultdict(set)
        for x, y in tmp:
            obstacles[x].add(y)
        del tmp

        def turnLeft(direction):
            if direction == 'N': return 'W'
            if direction == 'W': return 'S'
            if direction == 'S': return 'E'
            if direction == 'E': return 'N'

        def turnRight(direction):
            return turnLeft(turnLeft(turnLeft(direction)))

        def moveForward(pos):
            x, y, direction = pos
            if direction == 'N': x, y = x, y + 1
            if direction == 'W': x, y = x - 1, y
            if direction == 'S': x, y = x, y - 1
            if direction == 'E': x, y = x + 1, y
            if x not in obstacles or y not in obstacles[x]:
                pos[0], pos[1] = x, y
                return True
            return False

        result = 0
        pos = [0, 0, 'N']
        for cmd in commands:
            if cmd == -2:
                pos[2] = turnLeft(pos[2])
            elif cmd == -1:
                pos[2] = turnRight(pos[2])
            else:
                x, y, _ = pos
                for _ in range(cmd):
                    if not moveForward(pos):
                        break
                result = max(result, pos[0]**2 + pos[1]**2)
        return result
