# link: https://leetcode.com/problems/network-recovery-pathways/

from collections import defaultdict, deque


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # O((n + m) * log k) time and O(n + m) space
        n = len(online)
        graph = [defaultdict(list) for _ in range(n)]
        in_degrees = [0] * n
        for u, v, w in edges:
            if online[u] and online[v]:
                graph[u][v].append(w)
                in_degrees[v] += 1

        queue = deque(node for node in range(n) if in_degrees[node] == 0 and online[node])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for next in graph[node]:
                in_degrees[next] -= len(graph[node][next])
                if in_degrees[next] == 0:
                    queue.append(next)

        def canReach(min_score):
            dist = [10**21] * n
            dist[0] = 0
            for node in order:
                if node == n - 1: return dist[node] <= k
                if dist[node] > k: continue
                for next in graph[node]:
                    for w in graph[node][next]:
                        if w >= min_score:
                            dist[next] = min(dist[next], dist[node] + w)
            return False

        low, high = -1, k
        while low < high:
            mid = (low + high + 1) // 2
            if canReach(mid):
                low = mid
            else:
                high = mid - 1
        return low
