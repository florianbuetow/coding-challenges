# O(?) time and O(n) space
# link: https://adventofcode.com/2025/day/2

class Solution:
	def findInvalidIds(self, filename) -> int:
		def getIdRanges():
			id_ranges = []
			with open(filename, 'r') as fh:
				for line in fh:
					line = line.strip()
					for id_range in line.split(','):
						if id_range:
							id_range = [int(n) for n in id_range.split('-')]
							id_ranges.append(id_range)
			return id_ranges

		def isValidId(id):
			id = str(id)
			length = len(id)
			if length % 2 == 0:
				return id[:length//2] != id[length//2:]
			return True

		result = 0
		for id_start, id_end in getIdRanges():
			for id in range(id_start, id_end + 1):
				if not isValidId(id):
					result += id
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.findInvalidIds('input_0.txt'))
	print(s.findInvalidIds('input_1.txt'))

