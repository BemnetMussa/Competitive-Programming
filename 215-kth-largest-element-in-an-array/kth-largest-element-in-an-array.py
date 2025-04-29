class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(nums, n, i)
      
        ans = 0
        for _ in range(k):
            ans = self.heappop(nums)

        return ans
        

    def heappop(self, arr):
        # swap
        # pop
        # maintain the heap

        arr[0], arr[-1] = arr[-1], arr[0]
        max_val = arr.pop()

        self.heapify_down(arr, len(arr), 0)
        return max_val
    
 
    def heapify_down(self, arr, n, i):
       
        largest = i  
        left = 2 * i + 1  
        right = 2 * i + 2  

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than the largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If root is not the largest, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            self.heapify_down(arr, n, largest)