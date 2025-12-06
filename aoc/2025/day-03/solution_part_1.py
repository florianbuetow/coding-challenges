# O(n*m) time and O(n) space
# link: https://adventofcode.com/2025/day/3

class Solution:
	def maxJoltage(self, filename) -> int:

		def computeMaxJoltage(bank):
			max_battery_one = [-1, -1]
			for pos in range(len(bank)-2,-1,-1):
				joltage = int(bank[pos])
				if max_battery_one[0] <= joltage:
					max_battery_one = [joltage, pos]
			max_battery_two = [-1, -1]
			for pos in range(max_battery_one[1]+1, len(bank)):
				joltage = int(bank[pos])
				if max_battery_two[0] <= joltage:
					max_battery_two = [joltage, pos]
			return int(f"{max_battery_one[0]}{max_battery_two[0]}")

		result = 0
		with open(filename, 'r') as fh:
			for bank in fh:
				result += computeMaxJoltage(bank.strip())
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.maxJoltage('input_0.txt'))
	print(s.maxJoltage('input_1.txt'))

