class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # O(n*m) time and O(m) space, n=len(key), m=len(ring)
        # link: https://leetcode.com/problems/freedom-trail/

        def indexCharacterPositions():
            letters = {}
            for i, c in enumerate(ring):
                if c not in letters: letters[c] = []
                letters[c].append(i)
                letters[c].append(i + len(ring))
                letters[c].append(i - len(ring))
            for c in letters:
                letters[c] = sorted(letters[c])
            return letters

        def findClosest(pos_curr, positions):
            pos_left = pos_right = None
            for pos_next in positions:
                if pos_next < pos_curr:
                    pos_left = pos_next
                if pos_next == pos_curr: return [pos_curr]
                if pos_next > pos_curr:
                    pos_right = pos_next
                    break
            pos_left = (pos_left + len(ring)) % len(ring)
            pos_right = (pos_right + len(ring)) % len(ring)
            if pos_left == pos_right:
                return [pos_left]
            return [pos_left, pos_right]

        characterPositions = indexCharacterPositions()
        curr_positions = {0: 0}
        for c in key:
            next_positions = {}
            for curr_pos in curr_positions:
                for next_pos in findClosest(curr_pos, characterPositions[c]):
                    turning_costs = min(abs(curr_pos - next_pos), len(ring) - abs(curr_pos - next_pos))
                    total_costs = curr_positions[curr_pos] + turning_costs + 1
                    if total_costs < next_positions.get(next_pos, float('inf')):
                        next_positions[next_pos] = total_costs
            curr_positions = next_positions

        return min(curr_positions.values())
