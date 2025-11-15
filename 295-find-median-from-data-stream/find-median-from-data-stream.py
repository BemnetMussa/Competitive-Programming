from heapq import heappush, heappop

class MedianFinder:
    '''
    median -> the middle value in sorted array
    since 10^4 calls will be applied, it should be efficient

    App:
        naive way: for each num, sort the array and get middle -> NOT efficient

    Efficient approach: using heap!
        - single heap won't help
        - use two heaps:
            -> minHeap (right) = holds larger half
            -> maxHeap (left) = holds smaller half (as negative)
            -> maintain diff <= 1
            -> max of left <= min of right
    '''

    def __init__(self):
        self.minHeap = []  # right
        self.maxHeap = []  # left

    def addNum(self, num: int) -> None:
        # insert into maxHeap (as negative for max behavior)
        heappush(self.maxHeap, -num)

        # ensure ordering: maxHeap root <= minHeap root
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            val = -heappop(self.maxHeap)
            heappush(self.minHeap, val)

        # balance sizes
        if len(self.maxHeap) - len(self.minHeap) > 1:
            val = -heappop(self.maxHeap)
            heappush(self.minHeap, val)
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]
