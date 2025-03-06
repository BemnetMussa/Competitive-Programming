class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        

        max_queue = deque() # decreasing order
        min_queue = deque() # increasing order

        ans = 0
        left = 0

        for right, val in enumerate(nums):
            
            while max_queue and val > max_queue[-1]:
                max_queue.pop()

            while min_queue and val < min_queue[-1]:
                min_queue.pop()
            
            max_queue.append(val)
            min_queue.append(val)

            while max_queue[0] - min_queue[0] > limit:
               
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                left += 1
             
  
            ans = max(right - left + 1, ans)

        return ans

        # [9, 2, 4, 7]
        #  |            