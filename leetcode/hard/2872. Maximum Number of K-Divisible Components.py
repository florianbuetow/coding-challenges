from typing import List
from collections import defaultdict

# O(n) time and O(n) space
# link: https://leetcode.com/problems/maximum-number-of-k-divisible-components/

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def buildGraph(edges):
            g = defaultdict(set)
            for u, v in edges:
                g[u].add(v)
                g[v].add(u)
            return g

        result, g = 0, buildGraph(edges)

        def helper(prev, curr):
            nonlocal result
            component_sum = values[curr]
            for next in g[curr]:
                if next != prev:
                    component_sum += helper(curr, next)
            component_sum %= k
            if component_sum == 0:
                result += 1
            return component_sum

        if helper(None, 0) % k != 0:
            return -1
        return result
