from typing import List

# O(n*m) time and space
# link: https://adventofcode.com/2025/day/6

class Solution:
	def doMathHomework(self, filename) -> int:
	
		def getLines() -> List[str]:
			with open(filename, 'r') as fh:
				lines = fh.readlines()
			# adjust for max width
			for i in range(len(lines)):
				lines[i] = lines[i].rstrip()
			max_width = max([len(line) for line in lines])
			for i in range(len(lines)):
				lines[i] += ' ' * (max_width - len(lines[i]))
			return lines

		lines = getLines()

		res = []
		op = None
		numbers = []
		for col in range(len(lines[0])-1,-1,-1):
			digits = []
			for row in range(len(lines)):
				digit = lines[row][col]
				if digit in '+*':
					op = digit
					break					
				if digit != ' ':
					digits.append(digit)
			if digits:
				numbers.append(int("".join(digits)))
			if op:
				res.append([0, 1][op == '*'])
				for n in numbers:
					res[-1] += [0, n][op == '+']
					res[-1] *= [1, n][op == '*']		
				numbers = []
				op = None
		return sum(res)


if __name__ == '__main__':
	s = Solution()
	print(s.doMathHomework('input_0.txt'))
	print(s.doMathHomework('input_1.txt'))


