class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        # 0, 1, 0, 1
        # 1, 1, 0, 0 -> ok
        #       1, 0
        # priority queue 

        ans = 0
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, -nums[i])
            if s[i] == "1":
                ans += -heapq.heappop(heap)

        return ans


            
        

