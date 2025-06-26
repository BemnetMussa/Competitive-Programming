class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n + 1)] # available seats
        heapify(self.seats)

    def reserve(self) -> int:
        return heappop(self.seats) # returing the smallest unresearved seat
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)