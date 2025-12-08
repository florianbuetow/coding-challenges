# O(n*n) time and O(n) space, n = number of lines / junction boxes
# link: https://adventofcode.com/2025/day/8

from heapq import heapify, heappop

class UnionFind:

	def __init__(self):
		self.id = {}

	def find(self, x):
		if x not in self.id:
			self.id[x] = x
		y = self.id.get(x)
		if x != y:
			y = self.find(y)
		return y

	def union(self, x, y):
		self.id[self.find(x)] = self.find(y)

class Solution:
	def computeLargestCircuits(self, filename) -> int:
		
		def loadJunctionBoxes():
			boxes = []
			with open(filename, 'r') as fh:
				for line in fh:
					line = line.strip()
					if line:
						boxes.append([int(value) for value in line.split(',')])
			return boxes
		
		def computeDistance(coords1, coords2):
			dist = 0
			for c1, c2 in zip(coords1, coords2):
				dist += abs(c1-c2) ** 2
			return dist ** 0.5

		boxes = loadJunctionBoxes()
		distances = []
		for i in range(len(boxes)):
			for j in range(i + 1, len(boxes)):
				edge = [i, j]
				dist = computeDistance(boxes[i], boxes[j])
				distances.append([dist, edge])
		heapify(distances)

		result = 0
		connected_circuits = UnionFind()		
		while distances:
			u, v = heappop(distances)[1]
			if connected_circuits.find(u) != connected_circuits.find(v):
				connected_circuits.union(u, v)
				result = boxes[u][0] * boxes[v][0]
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.computeLargestCircuits('input_0.txt'))
	print(s.computeLargestCircuits('input_1.txt'))


