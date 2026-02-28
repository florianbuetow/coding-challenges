# link: https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/


from collections import deque
from bisect import bisect_left, bisect_right

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # O(n) time and O(1) space
        def remove(arr, left, right):
            left = bisect_left(arr, left)
            right = bisect_right(arr, right)
            result = arr[left:right]
            del arr[left:right]
            return result

        num_zeros = s.count('0')
        if num_zeros == 0: return 0
        memory = [[],[]]
        for i in range(len(s) // 2 + 1):
            memory[0].append(i * 2)
            memory[1].append(i * 2 + 1)
        q = deque([(num_zeros, 0)])
        visited = [False] * (len(s) + 1)
        visited[num_zeros] = True

        while q:
            z1, d = q.popleft()
            left = z1 + k - 2 * min(k, z1)
            right = z1 + k - 2 * max(0, k - (len(s) - z1))
            next_states = remove(memory[(z1 + k) % 2], max(0, left), min(len(s), right))
            for z2 in next_states:
                if visited[z2]: continue
                if z2 == 0: return d + 1
                visited[z2] = True
                q.append((z2, d + 1))
        return -1
