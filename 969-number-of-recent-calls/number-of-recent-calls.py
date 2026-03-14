class RecentCounter:

    def __init__(self):
        self.array = []

    def ping(self, t: int) -> int:
        self.array.append(t)
        while (t-self.array[0]) > 3000:
            self.array.pop(0)

        return len(self.array)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)