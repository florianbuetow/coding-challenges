# link: https://leetcode.com/problems/design-task-manager/


from heapq import heappush, heappop, heapify
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # O(n) time and O(1) space
        self.heap = []
        self.task_to_user = {}
        self.task_to_prio = {}
        for userId, taskId, priority in tasks:
            self.task_to_user[taskId] = userId
            self.task_to_prio[taskId] = priority
            self.heap.append([-priority, -taskId])
        heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # O(n) time and O(1) space
        heappush(self.heap, [-priority, -taskId])
        self.task_to_user[taskId] = userId
        self.task_to_prio[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:
        # O(n) time and O(1) space
        userId = self.task_to_user[taskId]
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        # O(n) time and O(1) space
        self.task_to_prio[taskId] = float('inf')

    def execTop(self) -> int:
        # O(n) time and O(1) space
        userId = -1
        while self.heap and userId == -1:
            priority, taskId = heappop(self.heap)
            priority, taskId = -priority, -taskId
            if taskId not in self.task_to_prio: continue
            if priority == self.task_to_prio[taskId]:
                userId = self.task_to_user[taskId]
                self.rmv(taskId)
                del self.task_to_prio[taskId]
                del self.task_to_user[taskId]
        return userId
