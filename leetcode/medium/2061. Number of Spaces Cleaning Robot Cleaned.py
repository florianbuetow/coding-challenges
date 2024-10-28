class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        # O(n * m) time and space
        # link: https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/
        width, height = len(room[0]), len(room)

        def getDeltaXY(d):
            d = d % 4
            if d == 0: return 1, 0 # go right
            if d == 1: return 0, 1 # do down
            if d == 2: return -1, 0 # go left
            if d == 3: return 0, -1 # go up

        def isValidLocation(x, y):
            # check if in bounds
            if x < 0 or x >= width: return False
            if y < 0 or y >= height: return False
            # check if free cell
            return room[y][x] == 0

        def updatePosition(pos):
            x, y, d = pos
            for _ in range(4):
                dx, dy = getDeltaXY(d)
                nx, ny = x + dx, y + dy
                if isValidLocation(nx,ny):
                    return (nx, ny, d)
                d = (d + 1) % 4
            return (x, y, d)

        visited = set()
        pos = (0,0,0) # x, y, direction
        while pos not in visited:
            visited.add(pos)
            pos = updatePosition(pos)

        # return number of unique positions
        return len(set((x,y) for x, y, _ in visited))
