# O(n*n) time and O(n) space
# link: https://adventofcode.com/2025/day/9

class Solution:
	def largestRectangleOfRedTiles(self, filename) -> int:

		def loadRedTiles():
			tiles = []
			with open(filename, "r") as fh:
				for line in fh:
					line = line.strip()
					if line:
						x, y = [int(value) for value in line.split(',')]
						tiles.append([x, y])
			return tiles

		def getArea(p1, p2):
			return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

		result = 0
		tiles = loadRedTiles()
		for i in range(len(tiles)):
			for j in range(i + 1, len(tiles)):
				result = max(result, getArea(tiles[i], tiles[j]))
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.largestRectangleOfRedTiles('input_0.txt'))
	print(s.largestRectangleOfRedTiles('input_1.txt'))


