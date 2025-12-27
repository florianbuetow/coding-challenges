# O(m log m) time and O(n) space
# link: https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        used_rooms = []
        unused_rooms = [room_id for room_id in range(n)]
        heapify(unused_rooms)
        meeting_count = [0] * n

        for t_start, t_end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= t_start:
                _, room_id = heappop(used_rooms)
                heappush(unused_rooms, room_id)

            if unused_rooms:
                room_id = heappop(unused_rooms)
                heappush(used_rooms, [t_end, room_id])
            else:
                room_availability_time, room_id = heappop(used_rooms)
                t_end_next = room_availability_time + t_end - t_start
                heappush(used_rooms, [t_end_next, room_id])
            meeting_count[room_id] += 1
        result = 0
        for room_id in range(n):
            if meeting_count[result] < meeting_count[room_id]:
                result = room_id
        return result
