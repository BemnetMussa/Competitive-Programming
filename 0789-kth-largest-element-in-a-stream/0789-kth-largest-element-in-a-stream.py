class KthLargest:
    '''
        constract a heap for nums[] 
        for each call return the kth largest element -> 

        add then kth largest elment -> O(n^2) 
        Reverse the logic  which will be for each call max call will be 1
    '''
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)