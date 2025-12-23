# O(n log n) time and O(n) space
# link: https://leetcode.com/problems/two-best-non-overlapping-events/description/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        memory = [0] * len(events)
        end_order = []
        for i in range(len(events)):
            end_order.append((events[i][1], i))
        end_order.sort(reverse=True)

        next, max_next_val = len(events) - 1, 0
        for end_time, curr in end_order:
            memory[curr] = events[curr][2]
            while next >= 0:
                if events[next][0] <= end_time:
                    break
                max_next_val = max(max_next_val, events[next][2])
                next -= 1
            memory[curr] += max_next_val
        return max(memory)
