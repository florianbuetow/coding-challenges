# link: https://leetcode.com/problems/count-the-number-of-complete-components/

from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # O(n + m) time and space
        def buildGraph():
            g = {i: [] for i in range(n)}
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g

        def getComponent(g, v):
            component = set()
            stack = [v]
            while stack:
                v = stack.pop()
                if v in component: continue
                component.add(v)
                for u in g[v]:
                    if u not in component:
                        stack.append(u)
            return component

        def getComponents(g):
            components = []
            visited = set()
            for v in range(n):
                if v in visited: continue
                component = getComponent(g, v)
                visited.update(component)
                components.append(component)
            return components

        def isCompleteConnected(g, component):
            for v in component:
                if len(g[v]) != len(component) - 1:
                    return False
            return True

        g = buildGraph()
        result = 0
        for component in getComponents(g):
            if isCompleteConnected(g, component):
                result += 1
        return result
