# O(n*m) time and O(m) space, n = number of rows, m = row width
# link: https://adventofcode.com/2025/day/7

class Solution:
	def computeBeamSplits(self, filename) -> int:
		
		def getNextRow():
			with open(filename, 'r') as fh:
				for row in fh:
					row = row.strip()
					if row:
						yield row

		result = 0
		beams = set()
		for row in getNextRow():
			new_beams = set()
			for pos, c in enumerate(row):
				if c == 'S':
					new_beams.add(pos)
				if pos in beams:
					if c == '^':
						result += 1
						new_beams.add(pos-1)
						new_beams.add(pos+1)
					else:
						new_beams.add(pos)
			beams = new_beams
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.computeBeamSplits('input_0.txt'))
	print(s.computeBeamSplits('input_1.txt'))


