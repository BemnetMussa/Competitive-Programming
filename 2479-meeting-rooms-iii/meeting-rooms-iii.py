import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
        
        # Heap of available rooms by room number
        available = list(range(n))
        heapq.heapify(available)

        # Heap of occupied rooms: (end_time, room_number)
        busy = []

        # Count how many times each room is used
        freq = [0] * n

        for start, end in meetings:
            # Free up rooms whose meetings have ended
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # Use the smallest available room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Wait for the earliest room to become free
                end_time, room = heapq.heappop(busy)
                # Delay the meeting
                new_end = end_time + (end - start)
                heapq.heappush(busy, (new_end, room))
            freq[room] += 1

        # Find the room with the most meetings
        max_meetings = max(freq)
        for i in range(n):
            if freq[i] == max_meetings:
                return i
