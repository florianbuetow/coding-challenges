# O(n log n) time and O(n) space, n = number of lines in input file
# link: https://adventofcode.com/2025/day/5

from collections import defaultdict

class Solution:
	def countFreshIngredients(self, filename) -> int:

		def loadIngredients():
			id_ranges, ids_available = list(), list()
			with open(filename, 'r') as fh:
				for line in fh:
					line = line.strip()
					if not line: continue
					if '-' in line:
						id_range = [int(i) for i in line.split('-')]
						id_ranges.append(id_range)
					else:
						ids_available.append(int(line))
			return id_ranges, ids_available

		id_ranges, ids_available = loadIngredients()

		delta = defaultdict(int)
		for range_start, range_end in id_ranges:
			delta[range_start] += 1
			delta[range_end + 1] -= 1
		delta = [[id, delta[id]] for id in sorted(delta.keys(), reverse=True)]

		result = 0
		nesting = 0
		for id in sorted(ids_available):
			while delta and delta[-1][0] <= id:
				nesting += delta.pop()[1]
			if nesting > 0:
				result += 1
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.countFreshIngredients('input_0.txt'))
	print(s.countFreshIngredients('input_1.txt'))




