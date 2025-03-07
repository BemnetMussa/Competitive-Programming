from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.queue.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.queue.pop()
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.queue[0]
        return -1  # Return -1 or another value to indicate it's empty

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.queue[-1]
        return -1  # Return -1 or another value to indicate it's empty

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.k
