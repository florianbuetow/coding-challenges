# link: https://leetcode.com/problems/process-tasks-using-servers/

from heapq import heapify, heappush, heappop

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # O(n log n + m log n) time and O(n+m) space,  n = len(servers), m = len(tasks)
        
        length = len(servers)
        weights = {server_id: weight + server_id / length for server_id, weight in enumerate(servers)}        
        
        free_servers = [(weights[server_id], server_id) for server_id in range(length)]
        heapify(free_servers)

        heap = []
        task_idx = timestamp = 0
        result = [-1] * len(tasks)
        
        while task_idx < len(tasks):
            if not free_servers and heap:
                timestamp = max(timestamp, heap[0][0])
            else:
                timestamp = max(timestamp, task_idx)

            while heap and heap[0][0] <= timestamp:
                _, server_id = heappop(heap)
                heappush(free_servers, (weights[server_id], server_id))

            while free_servers and task_idx < len(tasks) and task_idx <= timestamp:
                _, server_id = heappop(free_servers)
                task_completion = timestamp + tasks[task_idx]
                heappush(heap, [task_completion, server_id])
                result[task_idx] = server_id
                task_idx += 1
            
        return result
