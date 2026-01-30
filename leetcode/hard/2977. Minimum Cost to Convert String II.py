# O(n * m^2 * log m) time and O(n^2 * m) space
# link: https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g = defaultdict(lambda: defaultdict(int))
        sub_lengths = set()
        for sub in original:
            sub_lengths.add(len(sub))

        for i, start in enumerate(original):
            end = changed[i]
            if end in g[start]:
                g[start][end] = min(g[start][end], cost[i])
            else:
                g[start][end] = cost[i]


        @cache
        def findMinCost(start, end):
            distance = defaultdict(lambda: float('inf'))
            distance[start] = 0
            heap = [(0, start)]
            while heap:
                min_dist, node_curr = heapq.heappop(heap)
                if node_curr == end:
                    return min_dist
                for node_next in g[node_curr]:
                    node_next_cost = g[node_curr][node_next]
                    node_next_cost_update = node_next_cost + min_dist
                    if node_next_cost_update < distance[node_next]:
                        distance[node_next] = node_next_cost_update
                        heapq.heappush(heap, (node_next_cost_update, node_next))
            return float('inf')

        @cache
        def costToMatch(i):
            cost_to_match = 0
            if i < len(target):
                if target[i] != source[i]:
                    cost_to_match = float('inf')
                else:
                    cost_to_match = costToMatch(i + 1)
                for l in sub_lengths:
                    cost_to_transition = findMinCost(source[i:i + l], target[i:i + l])
                    if cost_to_transition == float('inf'): continue
                    cost_to_match = min(cost_to_match, cost_to_transition + costToMatch(i + l))
            return cost_to_match

        result = costToMatch(0)
        if result == float('inf'):
            result = -1
        return result
