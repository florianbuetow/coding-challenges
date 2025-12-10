# O(n*m) time and O(m) space, n = num lines, m = max(line length)
# link: https://adventofcode.com/2025/day/10

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

class Solution:
    def computeFewestButtonPressesToActivateMachines(self, filename) -> int:

        def getNextMachine(filename):
            with open(filename, "r") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        parts = line.split()
                        joltage_switches = []
                        for toggle_switch in parts[1:-1]:
                            joltage_switch = {}
                            for button in toggle_switch[1:-1].split(','):
                                joltage_switch[int(button)] = 1
                            if joltage_switch:
                                joltage_switches.append(joltage_switch)

                        required_joltage = []
                        for joltage in parts[-1][1:-1].split(','):
                            if joltage:
                                required_joltage.append(int(joltage))

                        required_joltage = tuple(required_joltage)

                    yield [required_joltage, joltage_switches]

        def helper(goal_state, switches):            
            """
            Solve for minimum button presses using Integer Linear Programming.

            We need to find non-negative integers x_i such that:
            A @ x = b (where A is the button matrix, b is joltage requirements)
            and minimize sum(x)
            """
            n_counters = len(goal_state)
            n_buttons = len(switches)

            # Build the coefficient matrix A
            # A[i][j] = 1 if button j affects counter i, else 0
            A = np.zeros((n_counters, n_buttons), dtype=np.float64)
            for j, switch in enumerate(switches):
                for counter_idx, increment in switch.items():
                    if counter_idx < n_counters:
                        A[counter_idx][j] = increment

            b = np.array(goal_state, dtype=np.float64)

            # Use Mixed Integer Linear Programming (MILP) to solve
            # Minimize: sum of x (all button presses)
            # Subject to: A @ x = b, x >= 0, x integer

            c = np.ones(n_buttons)  # Objective: minimize sum of all x

            # Equality constraint: A @ x = b
            constraints = LinearConstraint(A, b, b)

            # Bounds: x >= 0 (no upper bound)
            bounds = Bounds(lb=0, ub=np.inf)

            # All variables are integers
            integrality = np.ones(n_buttons)  # 1 = integer variable

            result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)

            if result.success:
                return int(round(result.fun))            
            raise Exception("Could not reach goal state.")


        result = 0
        for machine in getNextMachine(filename):
            result += helper(machine[0], machine[1])

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.computeFewestButtonPressesToActivateMachines('input_0.txt'))
    print(s.computeFewestButtonPressesToActivateMachines('input_1.txt'))