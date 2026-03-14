
from collections import deque
class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value # 4
        self.k = k # 3
        self.queue = deque() # []

    def consec(self, num: int) -> bool:
        if self.value != num: # []
            self.queue.clear()
        else:
            self.queue.append(num)
            if len(self.queue) > self.k:
                self.queue.popleft()

            if len(self.queue) == self.k:
                return True

        return False

        
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)