# O(n log n) time and O(n) space, n = number of lines in input file
# link: https://adventofcode.com/2025/day/5

from collections import defaultdict

class Solution:
	def countFreshIngredients(self, filename) -> int:

		def loadIngredients():
			id_ranges = list()
			with open(filename, 'r') as fh:
				for line in fh:
					line = line.strip()
					if '-' in line:
						id_range = [int(i) for i in line.split('-')]
						id_ranges.append(id_range)
			return id_ranges

		id_ranges = loadIngredients()

		delta = defaultdict(int)
		for range_start, range_end in id_ranges:
			delta[range_start] += 1
			delta[range_end + 1] -= 1
		delta = [[id, delta[id]] for id in sorted(delta.keys())]

		result = 0
		start_id = None
		nesting = 0
		for id, diff in delta:
			if nesting == 0:
				start_id = id
			nesting += diff
			if nesting == 0:
				result += (id - start_id)
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.countFreshIngredients('input_0.txt'))
	print(s.countFreshIngredients('input_1.txt'))




