from typing import List


class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        # O(8^(n*m)) time and O(n*m) space
        # link: https://leetcode.com/problems/the-knights-tour/
        @cache
        def get_possible_moves(pos):
            moves = []
            for dx, dy in zip([2, -2, 2, -2, 1, -1, 1, -1], [1, 1, -1, -1, 2, 2, -2, -2]):
                move = (pos[0] + dx, pos[1] + dy)
                if move[0] < 0 or move[0] >= n: continue
                if move[1] < 0 or move[1] >= m: continue
                moves.append(move)
            return moves

        def helper(pos, path, visited):
            visited.add(pos)
            if len(visited) == n * m:
                return True  # all positions have been visited exactly once
            for move in get_possible_moves(pos):
                if move in visited: continue
                path.append(move)
                if helper(move, path, visited): return True
                path.pop()
            visited.remove(pos)
            return False

        result = [[0] * n for _ in range(m)]
        pos = (c, r)
        path = [pos]
        if helper(pos, path, set()):
            for index, pos in enumerate(path):
                result[pos[1]][pos[0]] = index
        return result