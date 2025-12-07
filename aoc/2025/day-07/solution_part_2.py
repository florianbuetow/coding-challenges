# O(n*m) time and O(m) space, n = number of rows, m = row width
# link: https://adventofcode.com/2025/day/7

from collections import defaultdict

class Solution:
	def computeBeamSplits(self, filename) -> int:

		def getNextRow():
			with open(filename, 'r') as fh:
				for row in fh:
					row = row.strip()
					if row:
						yield row

		beams = defaultdict(int)
		for row in getNextRow():
			new_beams = defaultdict(int)
			for pos, c in enumerate(row):
				timelines = beams[pos]
				if c == 'S':
					new_beams[pos] = 1
				elif c == '^':
					new_beams[pos-1] += timelines
					new_beams[pos+1] += timelines
				else:
					new_beams[pos] += timelines
			beams = new_beams
		return sum(beams.values())

if __name__ == '__main__':
	s = Solution()
	print(s.computeBeamSplits('input_0.txt'))
	print(s.computeBeamSplits('input_1.txt'))


