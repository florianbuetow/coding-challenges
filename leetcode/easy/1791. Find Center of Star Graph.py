from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # O(1) time and O(1) space
        counter = defaultdict(int)
        counter[edges[0][0]] += 1
        counter[edges[0][1]] += 1
        counter[edges[1][0]] += 1
        counter[edges[1][1]] += 1
        result = edges[0][0]
        for node in counter:
            if counter[result] < counter[node]:
                result = node
        return result