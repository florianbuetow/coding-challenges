from typing import List

# O(n*m) time and O(m) space
# link: https://adventofcode.com/2025/day/6

class Solution:
	def doMathHomework(self, filename) -> int:
	
		def getOperators() -> List[str]:
			operators = None
			with open(filename, 'r') as fh:
				for line in fh:
					operators = line
			return [c for c in operators if c in '+*']

		def getNumbers() -> List[int]:
			with open(filename, 'r') as fh:
				for line in fh:
					if line[0] not in '+*':
						numbers = line.split(' ')
						numbers = [int(n) for n in numbers if n.strip()]
						yield numbers

		ops = getOperators()
		res = [[0, 1][op=='*'] for op in ops]
		for numbers in getNumbers():
			for i in range(len(res)):
				if ops[i] == '+':
					res[i] += numbers[i]
				else:
					res[i] *= numbers[i]
		return sum(res)


if __name__ == '__main__':
	s = Solution()
	print(s.doMathHomework('input_0.txt'))
	print(s.doMathHomework('input_1.txt'))


