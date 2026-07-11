# link: https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # O((n + q) log n) time and O(n log n) space
        sorted_nums = sorted(enumerate(nums), key=lambda e: e[1])
        rank = [0] * n
        for i, (original, _) in enumerate(sorted_nums):
            rank[original] = i

        MAX_LOG = 18
        jump = [[0] * MAX_LOG for _ in range(n)]

        right = 0
        for i in range(n):
            if right < i: right = i
            while (right + 1 < n and
                   sorted_nums[right + 1][1] - sorted_nums[right][1] <= maxDiff and
                   sorted_nums[right + 1][1] - sorted_nums[i][1] <= maxDiff):
                right += 1
            jump[i][0] = right

        for level in range(1, MAX_LOG):
            for i in range(n):
                jump[i][level] = jump[jump[i][level - 1]][level - 1]

        result = []
        for u, v in queries:
            start, end = rank[u], rank[v]
            if start > end: start, end = end, start
            if start == end:
                result.append(0)
                continue

            node, steps = start, 0
            for level in range(MAX_LOG - 1, -1, -1):
                if jump[node][level] < end:
                    node = jump[node][level]
                    steps += 1 << level

            result.append(steps + 1 if jump[node][0] >= end else -1)
        return result
