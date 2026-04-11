# link: https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot:
    def __init__(self, width: int, height: int):
        # O(1) time and space
        self.pos = [0, 0, 3]
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        # O(n + m) time and O(1) space, n = width, m = heighta

        def getMaxSteps(steps):
            dx = dy = 0
            x, y, d = self.pos
            if d == 0: dy = min(y + steps, self.height - 1) - y   # North
            if d == 1: dx = max(x - steps, 0) - x                 # West
            if d == 2: dy = max(y - steps, 0) - y                 # South
            if d == 3: dx = min(x + steps, self.width - 1) - x    # East
            return dx, dy

        perimeter = 2 * (self.width - 1 + self.height - 1)
        num %= perimeter
        if num == 0: num = perimeter
        while num > 0:
            dx, dy = getMaxSteps(num)
            if dx == 0 and dy == 0:
                self.pos[2] = (self.pos[2] + 1) % 4
            else:
                self.pos[0] += dx
                self.pos[1] += dy
                num -= abs(dx) + abs(dy)

    def getPos(self) -> list[int]:
        return self.pos[:2]

    def getDir(self) -> str:
        return ["North", "West", "South", "East"][self.pos[2]]
