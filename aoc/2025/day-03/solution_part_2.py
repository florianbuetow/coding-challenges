# O(n*m) time and O(n) space
# link: https://adventofcode.com/2025/day/3

class Solution:
	def maxJoltage(self, filename) -> int:
		num_batteries = 12

		def computeMaxJoltage(bank):
			max_battery = [[-1,-1] for _ in range(num_batteries)]
			for k in range(num_batteries):
				min_pos = -1 if k == 0 else max_battery[k-1][1]
				max_pos = len(bank) - (num_batteries - k)
				for pos in range(max_pos, min_pos,-1):
					joltage = int(bank[pos])
					if joltage >= max_battery[k][0]:
						max_battery[k] = [joltage, pos]
			return int(''.join([str(battery[0]) for battery in max_battery]))

		result = 0
		with open(filename, 'r') as fh:
			for bank in fh:
				result += computeMaxJoltage(bank.strip())
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.maxJoltage('input_0.txt'))
	print(s.maxJoltage('input_1.txt'))

