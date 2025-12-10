# O(n*m) time and O(m) space, n = num lines, m = max(line length)
# link: https://adventofcode.com/2025/day/10

from collections import deque, defaultdict

class Solution:
	def computeFewestButtonPressesToActivateMachines(self, filename) -> int:

		def getNextMachine():
			with open(filename, "r") as fh:
				for line in fh:
					line = line.strip()
					if line:
						parts = line.split()
						indicator = parts[0][1:-1][::-1]
						indicator = indicator.replace('.', '0')
						indicator = indicator.replace('#', '1')
						indicator_bitmask = int(indicator, 2)

						ops_bitmasks = []
						for toggle_switch in parts[1:-1]:
							buttons = []
							for button in toggle_switch[1:-1].split(','):
								buttons.append(int(button))
							buttons.sort(reverse=True)

							bitmask = ['0'] * (max(buttons) + 1)
							for button in buttons:
								bitmask[button] = '1'
							bitmask = ''.join(bitmask[::-1])
							ops_bitmasks.append(int(bitmask, 2))

					yield [indicator_bitmask, ops_bitmasks]

		def bfsHelper(goal_state, ops):
			q = deque([0])
			visited = set()
			iterations = 0
			while q:
				for _ in range(len(q)):
					state = q.popleft()
					if state == goal_state:
						return iterations
					if state not in visited:
						visited.add(state)
						for op in ops:
							q.append(state ^ op)
				iterations += 1
			raise Exception("Could not reach goal state.")

		result = 0
		for machine in getNextMachine():
			result += bfsHelper(machine[0], machine[1])
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.computeFewestButtonPressesToActivateMachines('input_0.txt'))
	print(s.computeFewestButtonPressesToActivateMachines('input_1.txt'))


