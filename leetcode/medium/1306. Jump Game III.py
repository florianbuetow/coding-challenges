# link: https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # O(n) time and space
        def find_zero(node, visited):
            if 0 <= node < len(arr) and node not in visited:
                visited.add(node)
                jump_distance = arr[node]
                if jump_distance == 0:
                    return True
                for next_node in [node - jump_distance, node + jump_distance]:
                    if find_zero(next_node, visited):
                        return True
            return False

        return find_zero(start, set())
