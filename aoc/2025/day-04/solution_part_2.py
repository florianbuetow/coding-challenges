# O(?) time and O(n*m) space
# link: https://adventofcode.com/2025/day/4

from collections import deque

class Grid:

	def __init__(self, grid):
		self.grid = grid
		self.width = len(grid[0])
		self.height = len(grid)

	def getNeighbors(self, x, y):
		neighbors = []
		for dx in [-1,0,1]:
			for dy in [-1,0,1]:
				nx, ny = x + dx, y + dy
				if dx == 0 and dy == 0: continue
				if nx < 0 or nx >= self.width: continue
				if ny < 0 or ny >= self.height: continue
				neighbors.append([nx, ny])
		return neighbors

	def getOccupiedNeighbors(self, x, y):
		occupiedNeighbors = []
		for nx, ny in self.getNeighbors(x, y):
			if self.isOccupied(nx, ny):
				occupiedNeighbors.append([nx, ny])
		return occupiedNeighbors

	def isOccupied(self, x, y):
		return self.grid[y][x]

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def setFree(self, x, y):
		self.grid[y][x] = False

class Solution:
	def forkliftAccess(self, filename) -> int:

		def loadGrid() -> Grid:
			grid = []
			with open(filename, 'r') as fh:
				for row in fh:
					row = row.strip()
					if row:
						grid.append([])
						for cell in row:
							grid[-1].append(cell == '@')
			return Grid(grid)

		result = 0
		grid: Grid = loadGrid()
		
		q = deque()		
		for y in range(grid.getHeight()):
			for x in range(grid.getWidth()):
				if grid.isOccupied(x, y):
					q.append([x, y])
		while q:
			x, y = q.popleft()
			if grid.isOccupied(x, y):
				occupiedNeighbors = grid.getOccupiedNeighbors(x, y)
				if len(occupiedNeighbors) < 4:
					grid.setFree(x, y)
					for neighbor in occupiedNeighbors:
						q.appendleft(neighbor)
					result += 1
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.forkliftAccess('input_0.txt'))
	print(s.forkliftAccess('input_1.txt'))




