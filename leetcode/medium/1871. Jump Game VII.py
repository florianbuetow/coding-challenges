# link: https://leetcode.com/problems/jump-game-vii/

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # O(n) time and space
        if s[-1] == '1': return False
        q = deque([0])
        furthest = 0
        while q:
            i = q.popleft()
            if i == len(s) - 1: return True
            minj = max(i + minJump, furthest)
            maxj = min(i + maxJump, len(s) - 1)
            for j in range(minj, maxj + 1):
                if s[j] == '0':  q.append(j)
            furthest = max(furthest, maxj + 1)
        return False
