# O((V+E) log V) time and O(V+E) space
# link: https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist = defaultdict(lambda:float('inf'))
        g = defaultdict(set)
        for u, v, w in edges:
            g[u].add((w, v))
            g[v].add((2 * w, u))

        q = [(0, 0)]
        while q:
            curr_dist, u = heappop(q)
            if curr_dist > dist[u]: continue
            if u == n - 1:  return curr_dist
            for w, v in g[u]:
                next_dist = curr_dist + w
                if next_dist < dist[v]:
                    dist[v] = next_dist
                    heappush(q, (next_dist, v))
        return -1
