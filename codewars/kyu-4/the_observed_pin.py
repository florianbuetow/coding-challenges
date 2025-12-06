# O(n) time and space, n = len(observed)
# Link: https://www.codewars.com/kata/5263c6999e0f40dee200059d

class Solution:

    def get_pins(self, observed):
        grid = [
            list('123'),
            list('456'),
            list('789'),
            list(' 0 ')
        ]
        alternatives = {str(n): [] for n in range(10)}
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):            
                if cell == ' ': continue
                for dx, dy in zip([-1,0,1,0,0], [0,-1,0,1,0]):
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx > 2: continue
                    if ny < 0 or ny > 3: continue
                    neighbor_cell = grid[ny][nx]
                    if neighbor_cell != ' ':
                        alternatives[cell].append(neighbor_cell)
        
        def helper(observed, idx, path, result):
            if idx >= len(observed):
                result.add("".join(path))
            else:
                for n in alternatives[observed[idx]]:
                    path.append(n)
                    helper(observed, idx + 1, path, result)
                    path.pop()
            return result    

        return helper(observed, 0, [], set())   


if __name__ == '__main__':

    test_cases = [
        ('8', ['5','7','8','9','0']),
        ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
        ('369', [
            "339","366","399","658","636","258","268","669","668","266","369","398",
            "256","296","259","368","638","396","238","356","659","639","666","359",
            "336","299","338","696","269","358","656","698","699","298","236","239"
        ])
    ]

    s = Solution()        
    for pin, expected in test_cases:        
        actual = sorted(s.get_pins(pin))
        exp = sorted(expected)
        pass_or_fail = ['PASSED', 'FAILED'][actual != exp]
        print(f"Test for PIN: {pin} -> {pass_or_fail}")
