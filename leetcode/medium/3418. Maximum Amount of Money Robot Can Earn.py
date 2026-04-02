# link: https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # O(n * m) time and space
        width, height = len(coins[0]), len(coins)
        memory = []
        for _ in range(height):
            memory.append([])
            for _ in range(width):
                memory[-1].append([float('inf'),float('inf'),float('inf')])

        def helper(x, y, remainingskips):
            if x >= width or y >= height or remainingskips < 0:
                return -float('inf')

            if x == width - 1 and y == height - 1:
                if coins[y][x] < 0 and remainingskips > 0:
                    memory[y][x][remainingskips] = 0
                else:
                    memory[y][x][remainingskips] = coins[y][x]
                return memory[y][x][remainingskips]

            if memory[y][x][remainingskips] != float('inf'):
                return memory[y][x][remainingskips]

            res = coins[y][x] + max(
                helper(x, y + 1, remainingskips),
                helper(x + 1, y, remainingskips)
            )

            if coins[y][x] < 0:
                res = max(
                    helper(x, y + 1, remainingskips - 1),
                    helper(x + 1, y, remainingskips - 1),
                    res
                )
            memory[y][x][remainingskips] = res
            return res

        return helper(0, 0, 2)
