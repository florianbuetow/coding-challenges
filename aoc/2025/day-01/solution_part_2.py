# O(n) time and O(1) space
# link: https://adventofcode.com/2025/day/1

class Solution:
	def openSafe(self, filename) -> int:
		result = 0
		position = 50
		with open(filename, 'r') as fh:
			for line in fh:
				line = line.strip()
				direction, clicks = line[0], int(line[1:])
				if direction == 'R':
					while position + clicks >= 100:
						result += 1
						clicks -= 100
				else:
					clicks *= -1
					if position == 0: result -= 1
					while position + clicks <= 0:
						result += 1
						clicks += 100
				position += clicks
				position %= 100
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.openSafe('input_0.txt'))
	print(s.openSafe('input_1.txt'))

