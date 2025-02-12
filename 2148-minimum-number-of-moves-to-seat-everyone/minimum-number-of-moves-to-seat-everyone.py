class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        

        seats.sort()
        students.sort()

        ptr = ptr2 = 0

        op = 0
        while ptr < len(seats) and ptr < len(students):

            if seats[ptr] != students[ptr]:
                op += abs(seats[ptr] - students[ptr])
            ptr += 1
        

        return op