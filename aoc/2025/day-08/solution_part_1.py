# O(n*n) time and O(n) space, n = number of lines / junction boxes
# link: https://adventofcode.com/2025/day/8

from collections import defaultdict
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
	def computeLargestCircuits(self, filename, max_connections) -> int:
		
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


		connected_boxids = set()
		connected_circuits = UnionFind()
		for _ in range(max_connections):
			u, v = heappop(distances)[1]
			connected_boxids.add(u)
			connected_boxids.add(v)
			connected_circuits.union(u, v)

		circuits = defaultdict(int)
		for box_id in connected_boxids:
			circuit_id = connected_circuits.find(box_id)
			circuits[circuit_id] += 1		
		result = 0

		largest_circuits = [1] * min(len(boxes) - len(connected_boxids),3)
		for box_count in circuits.values():
			largest_circuits.append(box_count)
			if len(largest_circuits) > 3:
				largest_circuits.sort(reverse=True)
				largest_circuits.pop()
		
		result = [0, 1][len(largest_circuits)>0]
		for size in largest_circuits:
			result *= size
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.computeLargestCircuits('input_0.txt', 10))
	print(s.computeLargestCircuits('input_1.txt', 1000))


