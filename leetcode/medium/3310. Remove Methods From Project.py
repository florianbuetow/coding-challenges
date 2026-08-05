# link: https://leetcode.com/problems/remove-methods-from-project/

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # O(n^2) time and O(n) space

        def getGraph():
            g, p = {}, {}
            for u in range(n):
                g[u] = set()
                p[u] = set()
            for u, v in invocations:
                g[u].add(v)
                p[v].add(u)
            return g, p

        def findSuspicious(g, node):
            queue = deque([node])
            visited = set()
            while queue:
                u = queue.popleft()
                if u not in g: continue
                if u in visited: continue
                visited.add(u)
                for v in g[u]:
                    queue.append(v)
            return visited

        g, p = getGraph()
        suspicious = findSuspicious(g, k)
        for u in suspicious:
            for v in p[u]:
                if v not in suspicious: return list(range(n))
        return [u for u in range(n) if u not in suspicious]
