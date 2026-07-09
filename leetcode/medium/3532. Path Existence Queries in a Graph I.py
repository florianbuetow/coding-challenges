# link: https://leetcode.com/problems/path-existence-queries-in-a-graph-i/


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # O(n) time and space
        component_count = 1
        component = defaultdict(int)
        for i in range(len(nums)):
            if i > 0 and abs(nums[i-1] - nums[i]) > maxDiff:
                component_count += 1
            component[i] = component_count
        return [component[i] == component[j] for i, j in queries]
