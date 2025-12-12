# O(n log n + m) time and O(n + m) space, n = number of events, m = number of users
# link: https://leetcode.com/problems/count-mentions-per-user/

from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        result = defaultdict(int)

        offline_queue = []
        offline_users = set()
        offline_users_counter = defaultdict(int)
        all_users = set(range(numberOfUsers))

        normalized = []
        for msg, ts, arg in events:
            ts_int = int(ts)
            type_order = 0 if msg == "OFFLINE" else 1
            normalized.append((ts_int, type_order, msg, arg))
        normalized.sort()

        for ts, _, msg, mentions in normalized:
            while offline_queue and offline_queue[0][0] <= ts:
                _, user_id = heappop(offline_queue)
                offline_users_counter[user_id] -= 1
                if offline_users_counter[user_id] == 0:
                    del offline_users_counter[user_id]
                    offline_users.remove(user_id)

            if msg == "OFFLINE":
                user_id = int(mentions)
                heappush(offline_queue, (ts + 60, user_id))
                offline_users_counter[user_id] += 1
                offline_users.add(user_id)
            else:
                if mentions == "ALL":
                    user_ids = all_users
                elif mentions == "HERE":
                    user_ids = all_users - offline_users
                else:
                    tokens = mentions.split()
                    user_ids = [int(t[2:]) for t in tokens]
                for user_id in user_ids:
                    result[user_id] += 1

        return [result[i] for i in range(numberOfUsers)]
