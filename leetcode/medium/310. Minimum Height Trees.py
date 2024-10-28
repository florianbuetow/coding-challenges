from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # O(n*h) time and O(n) space
        # link: https://leetcode.com/problems/minimum-height-trees/
        def getGraph(edges):
            g = {}
            for u, v in edges:
                if u == v: continue
                if u not in g: g[u] = set()
                if v not in g: g[v] = set()
                g[u].add(v)
                g[v].add(u)
            return g

        def getDegree(g):
            return {node: len(neighbors) for node, neighbors in g.items()}

        if n == 1: return[0]
        g = getGraph(edges)
        degree = getDegree(g)
        q = deque([node for node in degree if degree[node] == 1])

        minh_roots = []
        while q:
            minh_roots = []
            for _ in range(len(q)):
                node = q.popleft()
                minh_roots.append(node)
                degree[node] -= 1
                for neighbor in g[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        q.append(neighbor)
        return minh_roots
